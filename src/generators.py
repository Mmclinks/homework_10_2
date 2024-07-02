from typing import Dict, Generator, Iterator, List


def filter_by_currency(
    transactions: List[Dict[str, Dict[str, Dict[str, str]]]],
    currency: str
) -> Iterator[Dict[str, Dict[str, Dict[str, str]]]]:
    """
    Filters transactions by the specified currency.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, str]]
) -> Generator[str, None, None]:
    """
    Возвращает описания транзакций.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(
    start: int,
    end: int
) -> Generator[str, None, None]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield ' '.join("{:016}".format(number)[i:i + 4] for i in range(0, 16, 4))
