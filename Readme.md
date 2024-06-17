# Проект- Виджет банковских операций клиента

## Описание:

Виджет,на Python, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:Mmclinks/feature-homework_10_1.git
```

1. Установите зависимости:
```
pip install
poetry install
```
## Использование:

Пример использования функции sort_by_date:

data = [
    {"id": 1, "date": "2024-06-12T10:30:00.000"},
    {"id": 2, "date": "2024-06-11T09:25:30.000"},
    {"id": 3, "date": "2024-06-13T12:45:15.000"}
]

1. Сортировка по возрастанию (по умолчанию)
sorted_data_ascending = sort_by_date(data)
print("По возрастанию:", sorted_data_ascending)

2. Сортировка по убыванию
sorted_data_descending = sort_by_date(data, ascending=False)
print("По убыванию:", sorted_data_descending)


## Лицензия:

Этот проект лицензирован по [лицензии MIT].