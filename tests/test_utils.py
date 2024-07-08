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
