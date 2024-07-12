import re

# def main():
#     csv_file = '/home/alex/Загрузки/transactions.csv'
#     json_file = '/home/alex/Загрузки/operations.json'
#     xlsx_file = '/home/alex/Загрузки/transactions_excel.xlsx'
from typing import Dict, List

from src.processing import filter_by_state, sort_by_date
from src.search import search_transactions
from src.utils import (
    count_operations_by_category,
    read_transactions_from_csv,
    read_transactions_from_json,
    read_transactions_from_xlsx,
)
from src.widget import get_date, mask_account_card


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        json_file_path = '/home/alex/Загрузки/operations.json'
        transactions = read_transactions_from_json(json_file_path)
        if not transactions:
            print("Программа: Не удалось прочитать транзакции из JSON-файла.")
            return
        file_type = "JSON"
    elif choice == '2':
        csv_file_name = '/home/alex/Загрузки/transactions.csv'
        transactions = read_transactions_from_csv(csv_file_name)
        if not transactions:
            print("Программа: Не удалось прочитать транзакции из CSV-файла.")
            return
        file_type = "CSV"
    elif choice == '3':
        xlsx_file_name = input("Введите имя XLSX-файла: ")
        transactions = '/home/alex/Загрузки/transactions_excel.xlsx'
        if not transactions:
            print("Программа: Не удалось прочитать транзакции из XLSX-файла.")
            return
        file_type = "XLSX"
    else:
        print("Программа: Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    state = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").upper()
    valid_states = {'EXECUTED', 'CANCELED', 'PENDING'}
    if state not in valid_states:
        print(f"Программа: Статус операции \"{state}\" недоступен.")
        return

    filtered_transactions = filter_by_state(transactions, state)

    print(f"Программа: Операции отфильтрованы по статусу \"{state}\".")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice.startswith('д'):
        ascending_choice = input("Отсортировать по возрастанию или по убыванию? ").lower()
        ascending = ascending_choice.startswith('п')
        filtered_transactions = sort_by_date(filtered_transactions, ascending)

    rubles_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if rubles_choice.startswith('д'):
        filtered_transactions = [t for t in filtered_transactions if t['operationAmount']['currency']['code'] == 'RUB']

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if search_choice.startswith('д'):
        search_str = input("Введите строку для поиска: ")
        filtered_transactions = search_transactions(filtered_transactions, search_str)

    print("Программа: Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for transaction in filtered_transactions:
        print(get_date(transaction['date']))
        print(transaction['description'])
        print(mask_account_card(transaction['account_number']))
        print(f"Сумма: {transaction['operationAmount']['amount']}"
              f" {transaction['operationAmount']['currency']['code']}\n")

if __name__ == "__main__":
    main()
