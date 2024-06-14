import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-06-12T10:30:00.000"},
        {"id": 2, "state": "PENDING", "date": "2024-06-11T09:25:30.000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-06-13T12:45:15.000"},
        {"id": 4, "state": "CANCELLED", "date": "2024-06-10T08:20:00.000"},
    ]


@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3]),
    ("PENDING", [2]),
    ("CANCELLED", [4]),
    ("NON_EXISTENT", [])
])
def test_filter_by_state(sample_data, state, expected_ids):
    filtered_data = filter_by_state(sample_data, state)
    filtered_ids = [item['id'] for item in filtered_data]
    assert filtered_ids == expected_ids


@pytest.mark.parametrize("ascending, expected_order", [
    (True, [4, 2, 1, 3]),
    (False, [3, 1, 2, 4])
])
def test_sort_by_date(sample_data, ascending, expected_order):
    sorted_data = sort_by_date(sample_data, ascending=ascending)
    sorted_ids = [item['id'] for item in sorted_data]
    assert sorted_ids == expected_order
