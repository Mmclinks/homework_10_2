import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    return [
        "1234567890123456",
        "6543210987654321",
        "1111222233334444"
    ]


@pytest.fixture
def account_numbers():

@pytest.mark.parametrize("card_number, expected",[
    ("1234567890123456", "123456 ****** 3456"),
    ("6543210987654321", "654321 ****** 4321"),
    ("1111222233334444", "111122 ****** 4444"),
])
def test_get_mask_card_number(card_number, expected):

def test_get_mask_card_number_short():

@pytest.mark.parametrize("account_num, expected", [
    ("1234567890", "******7890"),
    ("0987654321", "******4321"),
    ("1122334455", "******4455"),
])
def test_get_mask_account(account_num, expected):
    assert get_mask_account(account_num) == expected


if __name__ == "__main__":
    pytest.main()
