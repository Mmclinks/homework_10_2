from datetime import datetime
from typing import List, Dict


def filter_by_state(data: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], ascending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    """
    date_format = '%Y-%m-%dT%H:%M:%S.%f'
    sorted_data = sorted(data, key=lambda item: datetime.strptime(item['date'], date_format), reverse=not ascending)
    return sorted_data
