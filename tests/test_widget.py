import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("data,expected", [
    ("счет 12345678", "счет ****5678"),
    ("счет 87654321", "счет ****4321"),
    ("VISA 1234567890123456", "VISA 123456 ****** 3456"),
    ("MasterCard 6543210987654321", "MasterCard 654321 ****** 4321"),
    ("AMEX 1111222233334444", "AMEX 111122 ****** 4444"),
    ("неизвестный формат 12345678", "неизвестный формат 12345678"),
])
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2024-06-14T10:15:30.000000", "14.06.2024"),
    ("2023-05-13T09:14:29.000000", "13.05.2023"),
    ("2022-04-12T08:13:28.000000", "12.04.2022"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
