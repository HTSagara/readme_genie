import unittest
from unittest.mock import MagicMock, patch

from src.models.cohere_api import cohereAPI


class TestCohereAPI(unittest.TestCase):
    @patch("src.models.cohere_api.cohere.Client")
    def test_cohere_api(self, MockCohereClient):
        mock_client = MockCohereClient.return_value
        mock_client.generate.return_value.generations = [
            MagicMock(text="Generated README content")
        ]

        result = cohereAPI("fake_api_key", "Sample file content")
        self.assertEqual(
            result.generations[0].text, "Generated README content"
        )


if __name__ == "__main__":
    unittest.main()
