import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстуры для формирования входных данных для тестов
@pytest.fixture
def sample_data():
    return [
        {'state': 'EXECUTED', 'date': '2024-06-14T10:15:30.000000'},
        {'state': 'CANCELLED', 'date': '2023-05-13T09:14:29.000000'},
        {'state': 'EXECUTED', 'date': '2022-04-12T08:13:28.000000'},
        {'state': 'PENDING', 'date': '2021-03-11T07:12:27.000000'},
    ]


# Тесты для функции filter_by_state
@pytest.mark.parametrize("state,expected", [
    ('EXECUTED', [
        {'state': 'EXECUTED', 'date': '2024-06-14T10:15:30.000000'},
        {'state': 'EXECUTED', 'date': '2022-04-12T08:13:28.000000'},
    ]),
    ('CANCELLED', [
        {'state': 'CANCELLED', 'date': '2023-05-13T09:14:29.000000'},
    ]),
    ('PENDING', [
        {'state': 'PENDING', 'date': '2021-03-11T07:12:27.000000'},
    ]),
    ('UNKNOWN', []),
])
def test_filter_by_state(sample_data, state, expected):
    assert filter_by_state(sample_data, state) == expected


# Тесты для функции sort_by_date
def test_sort_by_date_ascending(sample_data):
    sorted_data = sort_by_date(sample_data, ascending=True)
    expected = [
        {'state': 'PENDING', 'date': '2021-03-11T07:12:27.000000'},
        {'state': 'EXECUTED', 'date': '2022-04-12T08:13:28.000000'},
        {'state': 'CANCELLED', 'date': '2023-05-13T09:14:29.000000'},
        {'state': 'EXECUTED', 'date': '2024-06-14T10:15:30.000000'},
    ]
    assert sorted_data == expected


def test_sort_by_date_descending(sample_data):
    sorted_data = sort_by_date(sample_data, ascending=False)
    expected = [
        {'state': 'EXECUTED', 'date': '2024-06-14T10:15:30.000000'},
        {'state': 'CANCELLED', 'date': '2023-05-13T09:14:29.000000'},
        {'state': 'EXECUTED', 'date': '2022-04-12T08:13:28.000000'},
        {'state': 'PENDING', 'date': '2021-03-11T07:12:27.000000'},
    ]
    assert sorted_data == expected
