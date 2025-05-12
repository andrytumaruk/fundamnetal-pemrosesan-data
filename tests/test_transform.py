import unittest
import pandas as pd
from utils.transform import transform_data

class TransformDataTests(unittest.TestCase):

    def setUp(self):
        # Data yang sering digunakan bisa disiapkan di sini
        self.valid_data = [
            {'title': 'Product A', 'price': '10000', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product B', 'price': '20000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Women'}
        ]
        self.invalid_price_data = [
            {'title': 'Product X', 'price': 'invalid_price', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'}
        ]

    def test_transform_data_valid_input(self):
        df = transform_data(self.valid_data)

        self.assertEqual(len(df), 2)
        self.assertIn('price', df.columns)
        self.assertIn('rating', df.columns)
        self.assertIn('timestamp', df.columns)
        self.assertGreater(df.loc[0, 'price'], 0)
        self.assertGreater(df.loc[0, 'rating'], 0)

    def test_transform_data_invalid_price(self):
        df = transform_data(self.invalid_price_data)
        self.assertEqual(len(df), 0)  # Harus dibuang karena harga tidak valid

if __name__ == '__main__':
    unittest.main()