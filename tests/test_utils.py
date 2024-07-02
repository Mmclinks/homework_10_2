import unittest
from unittest.mock import mock_open, patch

from src.utils import read_transactions_from_json


class TestUtils(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_read_transactions_from_json_valid_json(self, mock_builtin_open):
        transactions = read_transactions_from_json('dummy.json')
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['amount'], 100)
        self.assertEqual(transactions[0]['currency'], 'USD')

        mock_builtin_open.assert_called_once_with('dummy.json', 'r')  # Пример использования мока

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    def test_read_transactions_from_json_empty_json(self, mock_builtin_open):
        transactions = read_transactions_from_json('dummy.json')
        self.assertEqual(transactions, [])

        mock_builtin_open.assert_called_once_with('dummy.json', 'r')  # Пример использования мока

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_transactions_from_json_file_not_found(self, mock_builtin_open):
        transactions = read_transactions_from_json('non_existing.json')
        self.assertEqual(transactions, [])

        mock_builtin_open.assert_called_once_with('non_existing.json', 'r')  # Пример использования мока

    @patch('builtins.open', new_callable=mock_open, read_data='not_a_json')
    def test_read_transactions_from_json_invalid_json(self, mock_builtin_open):
        transactions = read_transactions_from_json('dummy.json')
        self.assertEqual(transactions, [])

        mock_builtin_open.assert_called_once_with('dummy.json', 'r')  # Пример использования мока

if __name__ == '__main__':
    unittest.main()
