from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data (List[Dict[str, Any]]): Список транзакций в виде словарей.
        state (str): Состояние транзакции для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        List[Dict[str, Any]]: Отфильтрованный список транзакций.
    """
    return [item for item in data if item.get('state') == state]


from datetime import datetime

def sort_by_date(data, ascending=True):
    date_format = '%Y-%m-%dT%H:%M:%S%z'  # Изменен формат для работы с ISO 8601

    sorted_data = sorted(data, key=lambda item: datetime.fromisoformat(item['date']), reverse=not ascending)
    return sorted_data