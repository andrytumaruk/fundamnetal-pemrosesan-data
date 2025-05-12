# test_extract.py
import unittest
from unittest.mock import patch, MagicMock
from utils.extract import scrape_main

class TestExtract(unittest.TestCase):

    @patch('utils.extract.requests.get')
    def test_scrape_main_success(self, mock_get):
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Test Product</h3>
                    <div class="price-container">$10</div>
                    <p>Rating: 5</p>
                    <p>Colors: Red, Blue</p>
                    <p>Size: M, L</p>
                    <p>Gender: Unisex</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        result = scrape_main(url)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['title'], 'Test Product')

    @patch('utils.extract.requests.get')
    def test_scrape_main_failure(self, mock_get):
        mock_get.side_effect = Exception("Network Error")
        with self.assertRaises(Exception):
            scrape_main("https://fake-url.com")


if __name__ == '__main__':
    unittest.main()