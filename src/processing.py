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


def sort_by_date(data: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.

    Args:
        data (List[Dict[str, Any]]): Список транзакций в виде словарей.
        ascending (bool): Флаг сортировки по возрастанию. По умолчанию True.

    Returns:
        List[Dict[str, Any]]: Отсортированный список транзакций.
    """
    date_format = '%Y-%m-%dT%H:%M:%S.%f'
    sorted_data = sorted(data, key=lambda item: datetime.strptime(item['date'], date_format), reverse=not ascending)
    return sorted_data
