import pytest
from src.widget import mask_account_card, get_date


# Фикстура для примеров входных данных для маскировки карт
@pytest.fixture
def card_data():
    return [
        ("Visa 4111111111111111", "Visa ****1111"),
        ("MasterCard 5500000000000004", "MasterCard ****0004"),
        ("American Express 378282246310005", "American Express ****0005")
    ]


# Фикстура для примеров входных данных для маскировки счетов
@pytest.fixture
def account_data():
    return [
        ("Счет 12345678901234567890", "Счет ****7890"),
        ("Счет 98765432109876543210", "Счет ****43210"),
        ("счет 11223344556677889900", "счет ****9900")
    ]


# Параметризованный тест для маскировки карт
@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa 4111111111111111", "Visa ****1111"),
    ("MasterCard 5500000000000004", "MasterCard ****0004"),
    ("American Express 378282246310005", "American Express ****0005"),
    ("Diners Club 30569309025904", "Diners Club ****5904")
])
def test_mask_card_number(mocker, input_data, expected_output):
    mocker.patch('masks.get_mask_card_number', return_value=expected_output.split(' ')[1])
    assert mask_account_card(input_data) == expected_output


# Параметризованный тест для маскировки счетов
@pytest.mark.parametrize("input_data, expected_output", [
    ("Счет 12345678901234567890", "Счет ****7890"),
    ("Счет 98765432109876543210", "Счет ****43210"),
    ("счет 11223344556677889900", "счет ****9900")
])
def test_mask_account_number(mocker, input_data, expected_output):
    mocker.patch('masks.get_mask_account', return_value=expected_output.split(' ')[1])
    assert mask_account_card(input_data) == expected_output


# Тест с фикстурой для маскировки карт
def test_mask_card_with_fixture(card_data, mocker):
    for input_data, expected_output in card_data:
        mocker.patch('masks.get_mask_card_number', return_value=expected_output.split(' ')[1])
        assert mask_account_card(input_data) == expected_output


# Тест с фикстурой для маскировки счетов
def test_mask_account_with_fixture(account_data, mocker):
    for input_data, expected_output in account_data:
        mocker.patch('masks.get_mask_account', return_value=expected_output.split(' ')[1])
        assert mask_account_card(input_data) == expected_output


# Параметризованный тест для функции get_date
@pytest.mark.parametrize("input_date_str, expected_output", [
    ("2024-06-12T10:30:00.000", "12.06.2024"),
    ("2023-01-01T00:00:00.000", "01.01.2023"),
    ("2022-12-31T23:59:59.999", "31.12.2022")
])
def test_get_date(input_date_str, expected_output):
    assert get_date(input_date_str) == expected_output
