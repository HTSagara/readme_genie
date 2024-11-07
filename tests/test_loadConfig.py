# test_loadConfig.py
import unittest
from unittest.mock import mock_open, patch

from loadConfig import load_config


class TestLoadConfig(unittest.TestCase):
    @patch.dict("os.environ", {}, clear=True)  # Clear all environment variables
    @patch("loadConfig.os.getenv", side_effect=lambda key, default=None: default)
    @patch("loadConfig.os.path.exists", return_value=False)  # No .toml file exists
    @patch("builtins.open", new_callable=mock_open, read_data="{}")  # Empty JSON config
    @patch(
        "loadConfig.toml.load", return_value={}
    )  # Mock toml.load to return empty dict
    def test_load_config_empty_file(
        self, mock_toml_load, mock_open_file, mock_exists, mock_getenv
    ):
        config = load_config()
        self.assertEqual(config, {})  # Expecting an empty config

    @patch.dict("os.environ", {}, clear=True)
    @patch("loadConfig.os.getenv", side_effect=lambda key, default=None: default)
    @patch("loadConfig.os.path.exists", return_value=True)  # File exists
    @patch(
        "builtins.open", new_callable=mock_open, read_data='{"api_key": "test_key"}'
    )  # JSON with api_key
    @patch(
        "loadConfig.toml.load", return_value={"api_key": "test_key"}
    )  # Mock config data
    def test_load_config_with_valid_data(
        self, mock_toml_load, mock_open_file, mock_exists, mock_getenv
    ):
        config = load_config()
        self.assertEqual(config.get("api_key"), "test_key")

    @patch.dict("os.environ", {}, clear=True)
    @patch("loadConfig.os.getenv", side_effect=lambda key, default=None: default)
    @patch("loadConfig.os.path.exists", return_value=False)  # No file exists
    @patch(
        "builtins.open", side_effect=FileNotFoundError
    )  # Simulate file not found error
    @patch(
        "loadConfig.toml.load", return_value={}
    )  # Mock toml.load to return empty dict
    def test_load_config_file_not_found(
        self, mock_toml_load, mock_open_file, mock_exists, mock_getenv
    ):
        config = load_config()
        self.assertEqual(config, {})  # Expecting an empty config


if __name__ == "__main__":
    unittest.main()
