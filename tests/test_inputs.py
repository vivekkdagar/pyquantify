import unittest
from unittest.mock import patch
from pyquantify.utils.input_handler import scrape_website  # Correct import path


class TestScrapeWebsite(unittest.TestCase):
    @patch('ppyquantify.utils.input_handler.requests.get')  # Correct module path
    def test_scrape_website_success(self, mock_get):
        # Mock response object
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = '<html><body><p>Hello, world!</p></body></html>'
        mock_get.return_value = mock_response

        # Call the function
        result = scrape_website('http://example.com')

        # Assert expected result
        self.assertEqual(result, 'Hello, world!')

    @patch('ppyquantify.utils.input_handler.requests.get')  # Correct module path
    def test_scrape_website_failure(self, mock_get):
        # Mock response object
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404  # Simulating a failure response
        mock_get.return_value = mock_response

        # Call the function
        result = scrape_website('http://example.com')

        # Assert expected result
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
