from src.search import search_transactions


def test_search_transactions():
    transactions = [
        {"id": 1, "description": "Payment for services", "amount": 100},
        {"id": 2, "description": "Refund for product", "amount": -50},
        {"id": 3, "description": "Payment for subscription", "amount": 200},
        {"id": 4, "description": "Service charge", "amount": -10}
    ]

    search_str = "payment"
    result = search_transactions(transactions, search_str)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

    search_str = "refund"
    result = search_transactions(transactions, search_str)
    assert len(result) == 1
    assert result[0]["id"] == 2

    search_str = "charge"
    result = search_transactions(transactions, search_str)
    assert len(result) == 1
    assert result[0]["id"] == 4

    search_str = "nonexistent"
    result = search_transactions(transactions, search_str)
    assert len(result) == 0
