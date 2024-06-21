import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    # Добавьте остальные транзакции для полноты тестов
]


def test_filter_by_currency():
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570


def test_transaction_descriptions():
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator():
    card_numbers = list(card_number_generator(1, 5))
    assert card_numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]


if __name__ == "__main__":
    pytest.main()
