import unittest
from unittest.mock import MagicMock, patch

from models.groq_api import groqAPI


class TestGroqAPI(unittest.TestCase):
    @patch("models.groq_api.Groq")
    def test_groq_api(self, MockGroq):
        mock_client = MockGroq.return_value
        mock_client.chat.completions.create.return_value.choices = [
            MagicMock(message=MagicMock(content="Generated README content"))
        ]

        result = groqAPI("fake_api_key", "https://api.groq.com", "Sample file content")
        self.assertEqual(result.choices[0].message.content, "Generated README content")


if __name__ == "__main__":
    unittest.main()
