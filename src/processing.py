from typing import List
from datetime import datetime


def filter_by_state(data: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[dict], ascending: bool = False) -> List[dict]:
    """
    Сортирует список словарей по ключу 'date'.
    """
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=not ascending)
    return sorted_data
