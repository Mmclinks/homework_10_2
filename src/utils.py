import json
from typing import Any, Dict, List


def read_transactions_from_json(json_file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
