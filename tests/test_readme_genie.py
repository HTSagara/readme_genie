# test_readme_genie.py
import sys
import unittest
from unittest.mock import patch

from src.readme_genie import CustomArgumentParser, main, parse_arguments


class TestReadmeGenie(unittest.TestCase):
    def setUp(self):
        # Backup original sys.argv
        self.original_argv = sys.argv

    def tearDown(self):
        # Restore original sys.argv
        sys.argv = self.original_argv

    @patch(
        "src.readme_genie.load_config", return_value={"api_key": "test_key"}
    )
    def test_parse_arguments_defaults(self, mock_load_config):
        """Test argument parsing with default configuration values."""
        test_args = ["file1.py", "file2.py"]
        sys.argv = ["src.readme_genie.py"] + test_args

        args = parse_arguments(mock_load_config())
        self.assertEqual(args.api_key, "test_key")
        self.assertEqual(args.files, test_args)
        self.assertEqual(args.output, "README.md")
        self.assertFalse(args.token_usage)

    @patch(
        "src.readme_genie.load_config",
        return_value={"api_key": "test_key", "output": "custom_output.md"},
    )
    def test_parse_arguments_custom_output(self, mock_load_config):
        """Test parsing with a custom output file specified in config."""
        test_args = ["file1.py", "file2.py", "-o", "output.md"]
        sys.argv = ["src.readme_genie.py"] + test_args

        args = parse_arguments(mock_load_config())
        # Command-line argument should override config
        self.assertEqual(args.output, "output.md")

    @patch(
        "src.readme_genie.load_config", return_value={"api_key": "test_key"}
    )
    def test_parse_arguments_token_usage(self, mock_load_config):
        """Test argument parsing when token usage flag is set."""
        test_args = ["file1.py", "file2.py", "--token-usage"]
        sys.argv = ["src.readme_genie.py"] + test_args

        args = parse_arguments(mock_load_config())
        self.assertTrue(args.token_usage)

    @patch("src.readme_genie.sys.exit")
    @patch("src.readme_genie.logger")
    def test_custom_argument_parser_error(self, mock_logger, mock_exit):
        """Test CustomArgumentParser error handling with logging and exit."""
        parser = CustomArgumentParser()
        parser.error("Test error")
        mock_logger.error.assert_called_with("Argument error: Test error")
        mock_exit.assert_called_once_with(1)

    @patch(
        "src.readme_genie.load_config",
        return_value={"api_key": "test_key", "base_url": "http://example.com"},
    )
    @patch("src.readme_genie.read_file_content", return_value="file content")
    @patch(
        "src.readme_genie.handle_api_request", return_value="response content"
    )
    @patch("src.readme_genie.process_and_save_readme")
    @patch("src.readme_genie.sys.exit")
    def test_main_successful_run(
        self,
        mock_exit,
        mock_process,
        mock_handle,
        mock_read_file,
        mock_load_config,
    ):
        """Test the main function's successful run path."""
        test_args = ["file1.py", "file2.py", "--output", "output.md"]
        sys.argv = ["src.readme_genie.py"] + test_args

        main()

        mock_read_file.assert_called_once_with(["file1.py", "file2.py"])
        mock_handle.assert_called_once_with(
            "test_key", "http://example.com", "file content"
        )
        mock_process.assert_called_once_with(
            "response content", "output.md", False
        )
        mock_exit.assert_called_once_with(0)


if __name__ == "__main__":
    unittest.main()
