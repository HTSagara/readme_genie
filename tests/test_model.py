# tests/test_model.py
# tests/test_model.py
import os
import sys
import unittest
from unittest.mock import MagicMock, mock_open, patch

# Add the project root to sys.path to ensure models import correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.model import (
    check_title,
    create_env,
    get_env,
    handle_api_request,
    process_and_save_readme,
    read_file_content,
    report_token_usage,
    selectModel,
)


class TestModelFunctions(unittest.TestCase):
    def test_get_env(self):
        # Test when .env exists
        with patch("os.path.isfile", return_value=True):
            self.assertTrue(get_env())
        # Test when .env does not exist
        with patch("os.path.isfile", return_value=False):
            self.assertFalse(get_env())

    @patch("builtins.open", new_callable=mock_open)
    def test_create_env(self, mock_file):
        """Test .env file creation with different models"""
        create_env("test_api_key", "https://api.test.com", "cohere")
        mock_file.assert_called_once_with(".env", "a")
        mock_file().write.assert_any_call("COHERE_API_KEY=test_api_key\n")
        mock_file().write.assert_any_call("COHERE_BASE_URL=https://api.test.com\n")

    def test_select_model(self):
        """Test model selection based on base_url"""
        self.assertEqual(selectModel("https://api.cohere.ai/v1"), "cohere")
        self.assertEqual(selectModel("https://api.groq.com"), "groq")

    @patch("builtins.open", new_callable=mock_open, read_data="test content")
    def test_read_file_content(self, mock_file):
        """Test reading multiple files"""
        file_content = read_file_content(["file1.py", "file2.py"])
        self.assertEqual(file_content, "test content\n\ntest content\n\n")

    @patch("models.model.selectModel", return_value="groq")
    @patch("models.model.groqAPI")
    @patch("models.model.cohereAPI")
    def test_handle_api_request(self, mock_cohereAPI, mock_groqAPI, mock_selectModel):
        """Test handle_api_request for Groq API"""
        handle_api_request("test_api_key", "https://api.groq.com", "file content")
        mock_groqAPI.assert_called_once_with(
            "test_api_key", "https://api.groq.com", "file content"
        )

        # Test handle_api_request for Cohere API
        mock_selectModel.return_value = "cohere"
        handle_api_request("test_api_key", "https://api.cohere.ai/v1", "file content")
        mock_cohereAPI.assert_called_once_with("test_api_key", "file content")

    def test_check_title(self):
        """Test if check_title correctly removes extra lines and retains markdown content."""
        input_content = "Extra text\n*Generated README Content*"
        result = check_title(input_content)
        # Update expected output
        self.assertEqual(result, "*Generated README Content*")

    # Adjust test_process_and_save_readme in tests/test_model.py
    @patch("builtins.open", new_callable=mock_open)
    def test_process_and_save_readme(self, mock_file):
        """Test if process_and_save_readme writes the correct content to the output file."""
        response = MagicMock()
        response.choices = [MagicMock()]
        response.choices[0].message.content = "*Groq Generated Content*"

        process_and_save_readme(response, "output.md", False)

        # Expect only the content write call, without looking for an empty call
        mock_file().write.assert_called_once_with("*Groq Generated Content*")

    @patch("models.model.logger")
    def test_report_token_usage(self, mock_logger):
        """Test successful token usage logging"""
        mock_response = MagicMock()
        mock_response.usage.prompt_tokens = 50
        mock_response.usage.completion_tokens = 30
        mock_response.usage.total_tokens = 80

        report_token_usage(mock_response)
        mock_logger.info.assert_any_call(
            "Token Usage Information: Prompt tokens: 50, Completion tokens: 30, Total tokens: 80"
        )

        # Test handling of missing usage attribute
        mock_response = MagicMock()
        del mock_response.usage  # Remove the usage attribute
        report_token_usage(mock_response)
        mock_logger.warning.assert_any_call(
            "Token usage information not available for this response."
        )


if __name__ == "__main__":
    unittest.main()
