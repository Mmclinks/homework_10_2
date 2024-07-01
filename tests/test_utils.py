import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.external_api import convert_amount_to_rubles
from src.utils import read_transactions_from_json


class TestUtils(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_read_transactions_from_json(self, mock_file):
        transactions = read_transactions_from_json('dummy.json')
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['amount'], 100)
        self.assertEqual(transactions[0]['currency'], 'USD')

    @patch('requests.get')
    @patch('os.getenv')
    def test_convert_amount_to_rubles(self, mock_getenv: MagicMock, mock_requests_get: MagicMock):
        mock_getenv.return_value = 'dummy_api_key'
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'rates': {'USD': 0.013, 'RUB': 1.0}}

        transaction = {'amount': '100', 'currency': 'USD'}
        converted_amount = convert_amount_to_rubles(transaction)
        self.assertAlmostEqual(converted_amount, 1.3, places=2)
