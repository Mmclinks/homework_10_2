import re
from typing import Dict, List


def search_transactions(transactions: List[Dict[str, str]], search_str: str) -> List[Dict[str, str]]:
    """
    Функция для поиска банковских операций по описанию.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_str: Строка поиска.
    :return: Список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(search_str, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]