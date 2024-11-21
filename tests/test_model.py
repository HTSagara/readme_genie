import os
import sys
import time
import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.models.model import (
    check_title,
    create_env,
    get_env,
    handle_api_request,
    process_and_save_readme,
    read_file_content,
    report_token_usage,
    selectModel,
)

# Add the project root to sys.path to ensure models import correctly
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


class TestModelFunctions(unittest.TestCase):
    def test_get_env(self):
        with patch("os.path.isfile", return_value=True):
            self.assertTrue(get_env())
        with patch("os.path.isfile", return_value=False):
            self.assertFalse(get_env())

    @patch("builtins.open", new_callable=mock_open)
    def test_create_env(self, mock_file):
        create_env("test_api_key", "https://api.test.com", "cohere")
        mock_file.assert_called_once_with(".env", "a")
        mock_file().write.assert_any_call("COHERE_API_KEY=test_api_key\n")
        mock_file().write.assert_any_call(
            "COHERE_BASE_URL=https://api.test.com\n"
        )

    def test_select_model(self):
        self.assertEqual(selectModel("https://api.cohere.ai/v1"), "cohere")
        self.assertEqual(selectModel("https://api.groq.com"), "groq")

    @patch("builtins.open", new_callable=mock_open, read_data="test content")
    def test_read_file_content(self, mock_file):
        file_content = read_file_content(["file1.py", "file2.py"])
        self.assertEqual(file_content, "test content\n\ntest content\n\n")

    @patch("src.models.model.selectModel", return_value="groq")
    @patch("src.models.model.groqAPI")
    @patch("src.models.model.cohereAPI")
    def test_handle_api_request(
        self, mock_cohereAPI, mock_groqAPI, mock_selectModel
    ):
        handle_api_request(
            "test_api_key", "https://api.groq.com", "file content"
        )
        mock_groqAPI.assert_called_once_with(
            "test_api_key", "https://api.groq.com", "file content"
        )

        mock_selectModel.return_value = "cohere"
        handle_api_request(
            "test_api_key", "https://api.cohere.ai/v1", "file content"
        )
        mock_cohereAPI.assert_called_once_with("test_api_key", "file content")

    def test_check_title(self):
        input_content = "Extra text\n*Generated README Content*"
        result = check_title(input_content)
        self.assertEqual(result, "*Generated README Content*")

    @patch("builtins.open", new_callable=mock_open)
    def test_process_and_save_readme(self, mock_file):
        response = MagicMock()
        response.choices = [MagicMock()]
        response.choices[0].message.content = "*Groq Generated Content*"

        process_and_save_readme(response, "output.md", False)
        mock_file().write.assert_called_once_with("*Groq Generated Content*")

    @patch("src.models.model.logger")
    def test_report_token_usage(self, mock_logger):
        mock_response = MagicMock()
        mock_response.usage.prompt_tokens = 50
        mock_response.usage.completion_tokens = 30
        mock_response.usage.total_tokens = 80

        report_token_usage(mock_response)
        mock_logger.info.assert_any_call(
            "Token Usage Information: Prompt tokens: 50, Completion tokens: 30, Total tokens: 80"
        )

        mock_response = MagicMock()
        del mock_response.usage
        report_token_usage(mock_response)
        mock_logger.warning.assert_any_call(
            "Token usage information not available for this response."
        )

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_file_content_empty_file(self, mock_file):
        """Test read_file_content with an empty file."""
        # Mock the behavior for an empty file
        file_content = read_file_content(["empty_file.py"])
        # Assert that the function includes newlines for empty content
        self.assertEqual(file_content, "\n\n")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="# This is a comment\n# Another comment line\n",
    )
    def test_read_file_content_only_comments(self, mock_file):
        """Test read_file_content with a file containing only comments."""
        # Mock the behavior for a file with only comments
        file_content = read_file_content(["comments_only.py"])
        # Assert that the comments are returned as part of the content
        self.assertEqual(
            file_content, "# This is a comment\n# Another comment line\n\n\n"
        )

    @patch(
        "builtins.open", new_callable=mock_open, read_data="line\n" * 10**6
    )  # Simulate 1 million lines
    def test_read_file_content_large_file(self, mock_file):
        """Test read_file_content with a large file."""
        start_time = time.time()

        file_content = read_file_content(["large_file.py"])

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Assert the content length matches the simulated file size
        expected_content = ("line\n" * 10**6) + "\n\n"
        self.assertEqual(file_content, expected_content)

        # Check performance (should complete within 2 seconds)
        self.assertLess(
            elapsed_time, 2, "Processing large files took too long!"
        )


if __name__ == "__main__":
    unittest.main()
