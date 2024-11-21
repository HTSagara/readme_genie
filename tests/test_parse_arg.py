# tests/test_parse_arg.py
import os
import sys
import unittest

# This is necessary because the test is in a subdirectory (tests), and Python wouldn’t find readme_genie.py by default.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)
from readme_genie import parse_arguments


class TestArgumentParsing(unittest.TestCase):
    def test_argument_parsing_with_defaults(self):
        """Test the argument parsing"""
        test_args = ["file1.py", "file2.py"]

        config = {
            "api_key": "test_key",
            "base_url": "https://api.test.com",
            "output": "README.md",
        }

        # Temporarily override sys.argv
        sys.argv = ["test_parse_arg.py"] + test_args
        args = parse_arguments(config)

        self.assertEqual(args.api_key, "test_key")
        self.assertEqual(args.base_url, "https://api.test.com")
        self.assertEqual(args.output, "README.md")
        self.assertEqual(
            args.files, test_args
        )  # Check the mock files are set correctly


if __name__ == "__main__":
    unittest.main()
