# import unittest
# from unittest.mock import mock_open, patch
#
# from src.utils import read_transactions_from_json
#
#
# class TestUtils(unittest.TestCase):
#
#     @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
#     def test_read_transactions_from_json_valid_json(self, mock_builtin_open):
#         transactions = read_transactions_from_json('dummy.json')
#         self.assertEqual(len(transactions), 1)
#         self.assertEqual(transactions[0]['amount'], 100)
#         self.assertEqual(transactions[0]['currency'], 'USD')
#
#         mock_builtin_open.assert_called_once_with('dummy.json', 'r')  # Пример использования мока
#
#     @patch('builtins.open', new_callable=mock_open, read_data='[]')
#     def test_read_transactions_from_json_empty_json(self, mock_builtin_open):
#         transactions = read_transactions_from_json('dummy.json')
#         self.assertEqual(transactions, [])
#
#         mock_builtin_open.assert_called_once_with('dummy.json', 'r')  # Пример использования мока
#
#     @patch('builtins.open', side_effect=FileNotFoundError)
#     def test_read_transactions_from_json_file_not_found(self, mock_builtin_open):
#         transactions = read_transactions_from_json('non_existing.json')
#         self.assertEqual(transactions, [])
#
#         mock_builtin_open.assert_called_once_with('non_existing.json', 'r')  # Пример использования мока
#
#     @patch('builtins.open', new_callable=mock_open, read_data='not_a_json')
#     def test_read_transactions_from_json_invalid_json(self, mock_builtin_open):
#         transactions = read_transactions_from_json('dummy.json')
#         self.assertEqual(transactions, [])
#
#         mock_builtin_open.assert_called_once_with('dummy.json', 'r')  # Пример использования мока
#
# if __name__ == '__main__':
#     unittest.main()
import json
import os
from typing import Any, Dict, List

from src.utils import read_transactions_from_json


# Вспомогательная функция для создания временного JSON-файла
def create_temp_json_file(data: Any, filename: str) -> str:
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    return file_path


def test_read_transactions_from_json_success():
    data: List[Dict[str, Any]] = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    file_path = create_temp_json_file(data, 'test_data.json')
    result = read_transactions_from_json(file_path)
    assert result == data
    os.remove(file_path)


def test_read_transactions_from_json_file_not_found():
    result = read_transactions_from_json('non_existing_file.json')
    assert result == []


def test_read_transactions_from_json_invalid_format():
    # Неверный формат: не список
    data: Dict[str, int] = {"id": 1, "amount": 100}
    file_path = create_temp_json_file(data, 'test_data_invalid.json')
    result = read_transactions_from_json(file_path)
    assert result == []
    os.remove(file_path)


def test_read_transactions_from_json_empty_list():
    # Верный формат: пустой список
    data: List[Dict[str, Any]] = []
    file_path = create_temp_json_file(data, 'test_data_empty.json')
    result = read_transactions_from_json(file_path)
    assert result == data
    os.remove(file_path)
