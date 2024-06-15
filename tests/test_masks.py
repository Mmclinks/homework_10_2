import pytest
from src.masks import get_mask_card_number, get_mask_account


# Фикстуры для формирования входных данных для тестов
@pytest.fixture
def valid_card_numbers():
    return [
        "1234567890123456",
        "6543210987654321",
        "1111222233334444",
    ]


@pytest.fixture
def valid_account_numbers():
    return [
        "12345678",
        "87654321",
        "1111222233334444",
    ]


# Тесты для функции get_mask_card_number
@pytest.mark.parametrize("card_number,expected", [
    ("1234567890123456", "123456******3456"),
    ("6543210987654321", "654321******4321"),
    ("1111222233334444", "111122******4444"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_short_number():
    with pytest.raises(ValueError, match="Номер карты слишком короткий."):
        get_mask_card_number("1234567890")


# Тесты для функции get_mask_account
@pytest.mark.parametrize("account_num,expected", [
    ("12345678", "****5678"),
    ("87654321", "****4321"),
    ("1111222233334444", "************4444"),
])
def test_get_mask_account(account_num, expected):
    assert get_mask_account(account_num) == expected
