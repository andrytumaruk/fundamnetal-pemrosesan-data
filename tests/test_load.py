# test_load.py
import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import save_to_csv, save_to_google_sheets

class TestLoad(unittest.TestCase):

    @patch('utils.load.pd.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        df = pd.DataFrame({'title': ['Product'], 'price': [10.0], 'rating': [5.0]})
        save_to_csv(df, 'test.csv')
        mock_to_csv.assert_called_once_with('test.csv', index=False)

    @patch('utils.load.build')
    @patch('utils.load.Credentials.from_service_account_file')
    def test_save_to_google_sheets(self, mock_creds, mock_build):
        df = pd.DataFrame({'title': ['Product'], 'price': [10.0], 'rating': [5.0]})
        mock_creds.return_value = MagicMock()
        mock_service = MagicMock()
        mock_build.return_value = mock_service

        save_to_google_sheets(df, 'spreadsheet_id', 'Sheet1!A1')
        mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()

if __name__ == '__main__':
    unittest.main()