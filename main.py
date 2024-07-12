import json

import pandas as pd

# Пути к файлам
JSON_FILE = 'data/operations.json'
CSV_FILE = 'transactions.csv'
XLSX_FILE = 'transactions.xlsx'


# Функция для чтения транзакций из различных форматов файлов
def read_transactions(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")


# Функция для вывода транзакций
def print_transactions(transactions):
    if isinstance(transactions, pd.DataFrame):
        for index, row in transactions.iterrows():
            print(f"{row['date']} {row['description']}")
            print(f"Счет {row['account']} -> {row['destination']}")
            print(f"Сумма: {row['amount']} {row['currency']}\n")
    elif isinstance(transactions, list):
        for transaction in transactions:
            print(transaction['date'], transaction['description'])
            print(transaction['source'], '->', transaction['destination'])
            print(f"Сумма: {transaction['amount']} {transaction['currency']}\n")


# Функция для фильтрации транзакций по статусу
def filter_transactions(transactions, state):
    normalized_status = state.lower()
    if isinstance(transactions, pd.DataFrame):
        return transactions[transactions["state"].str.lower() == normalized_status]
    elif isinstance(transactions, list):
        return [t for t in transactions if t["state"].lower() == normalized_status]
    else:
        raise TypeError("Unsupported transactions type")


# Основная функция
def main():
    global filtered_transactions
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = read_transactions(JSON_FILE)
    elif choice == '2':
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = read_transactions(CSV_FILE)
    elif choice == '3':
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = read_transactions(XLSX_FILE)
    else:
        print("Программа: Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    while True:
        status = input("Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
                       "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                       "Пользователь: ").strip().upper()

        if status in {'EXECUTED', 'CANCELED', 'PENDING'}:
            filtered_transactions = filter_transactions(transactions, status)
            print(f"Программа: Операции отфильтрованы по статусу \"{status}\".")
            break
        else:
            print(f"Программа: Статус операции \"{status}\" недоступен.")
            continue

    sort_by_date = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_by_date == 'да':
        ascending = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        if ascending == 'по возрастанию':
            filtered_transactions = filtered_transactions.sort_values(by='date', ascending=True)
        elif ascending == 'по убыванию':
            filtered_transactions = filtered_transactions.sort_values(by='date', ascending=False)
        else:
            print("Программа: Некорректный ввод. Сортировка не будет выполнена.")

    only_rubles = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if only_rubles == 'да':
        if isinstance(filtered_transactions, pd.DataFrame):
            filtered_transactions = filtered_transactions[filtered_transactions['currency'] == 'руб.']
        elif isinstance(filtered_transactions, list):
            filtered_transactions = [t for t in filtered_transactions if t['currency'] == 'руб.']

    filter_by_description = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if filter_by_description == 'да':
        keyword = input("Программа: Введите ключевое слово для фильтрации: ").strip().lower()
        if isinstance(filtered_transactions, pd.DataFrame):
            filtered_transactions = filtered_transactions[
                filtered_transactions['description'].str.lower().str.contains(keyword)]
        elif isinstance(filtered_transactions, list):
            filtered_transactions = [t for t in filtered_transactions if keyword in t['description'].lower()]

    if len(filtered_transactions) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Программа: Распечатываю итоговый список транзакций...\n")
        print_transactions(filtered_transactions)
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")


if __name__ == "__main__":
    main()
