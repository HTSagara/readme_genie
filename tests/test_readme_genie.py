# test_readme_genie.py
import sys
import unittest
from unittest.mock import patch

from readme_genie import parse_arguments


class TestReadmeGenie(unittest.TestCase):
    @patch("readme_genie.load_config", return_value={"api_key": "test_key"})
    def test_parse_arguments_defaults(self, mock_load_config):
        """Test argument parsing with default configuration values."""
        test_args = ["file1.py", "file2.py"]
        sys.argv = ["readme_genie.py"] + test_args

        args = parse_arguments(mock_load_config())
        self.assertEqual(args.api_key, "test_key")
        self.assertEqual(args.files, test_args)


if __name__ == "__main__":
    unittest.main()
