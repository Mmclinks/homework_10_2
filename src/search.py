import re
from typing import List, Dict

def search_transactions_by_regex(transactions: List[Dict[str, str]], search_str: str) -> List[Dict[str, str]]:
    """
    Функция для поиска банковских операций по описанию с использованием регулярных выражений.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_str: Строка поиска с использованием регулярного выражения.
    :return: Список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(search_str, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]
