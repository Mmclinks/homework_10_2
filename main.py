import logging
from collections import Counter
from src.processing import filter_by_state, sort_by_date
from src.utils import read_transactions_from_csv, read_transactions_from_json, read_transactions_from_xlsx
from src.masks import get_mask_account, get_mask_card_number

logging.basicConfig(level=logging.INFO)


def mask_account_card(data: str) -> str:
    if data.lower().startswith('счет'):
        parts = data.split(' ', 1)
        if len(parts) > 1:
            account_number = parts[1]
            masked_number = get_mask_account(account_number)
            return f"{parts[0]} {masked_number}"
        else:
            return data
    else:
        parts = data.rsplit(' ', 1)
        if len(parts) > 1:
            card_type = parts[0]
            card_number = parts[1]
            if len(card_number) == 16:
                masked_number = get_mask_card_number(card_number)
                masked_number = f"{masked_number[:6]} ****** {masked_number[-4:]}"
                return f"{card_type} {masked_number}"
            else:
                return data
        else:
            return data


def count_operations_by_category(operations, categories):
    category_counts = Counter()
    for operation in operations:
        if operation.get('category') in categories:
            category_counts[operation['category']] += 1
    return dict(category_counts)


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")

    transactions = None  # Инициализируем переменную transactions

    while True:
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Пользователь: ")

        if choice == '1':
            file_path = '/home/alex/Загрузки/operations.json'
            transactions = read_transactions_from_json(file_path)
            file_type = "JSON"
            break
        elif choice == '2':
            file_path = '/home/alex/Загрузки/transactions.csv'
            transactions = read_transactions_from_csv(file_path)
            file_type = "CSV"
            break
        elif choice == '3':
            file_path = '/home/alex/Загрузки/transactions_excel.xlsx'
            transactions = read_transactions_from_xlsx(file_path)
            file_type = "XLSX"
            break
        else:
            print("Программа: Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
            continue

    if transactions is None:
        print(f"Программа: Не удалось прочитать транзакции из {file_type}-файла.")
        return

    state = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").upper()
    valid_states = {'EXECUTED', 'CANCELED', 'PENDING'}
    while state not in valid_states:
        print(f"Программа: Статус операции \"{state}\" недоступен.")
        state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").upper()

    filtered_transactions = filter_by_state(transactions, state)
    print(f"Программа: Операции отфильтрованы по статусу \"{state}\".")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice.startswith('д'):
        ascending_choice = input("Отсортировать по возрастанию или по убыванию? ").lower()

        # Определяем направление сортировки по ответу пользователя
        if 'возрастанию' in ascending_choice:
            ascending = True
        elif 'убыванию' in ascending_choice:
            ascending = False
        else:
            print("Неверный ввод для порядка сортировки. Используется сортировка по возрастанию по умолчанию.")
            ascending = True  # По умолчанию сортировка по возрастанию

        # Сортируем транзакции по дате в соответствии с выбранным порядком
        filtered_transactions = sort_by_date(filtered_transactions, ascending)

    rubles_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if rubles_choice.startswith('д'):
        filtered_transactions = [t for t in filtered_transactions if
                                 t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']

    print("Программа: Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    for transaction in filtered_transactions:
        date = transaction.get('date', 'N/A')
        description = transaction.get('description', 'N/A')
        print(date)
        print(description)

        account_info = ""
        if 'from' in transaction and 'to' in transaction:
            account_info = f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}"
        elif 'from' in transaction:
            account_info = f"Со счета {mask_account_card(transaction['from'])}"
        elif 'to' in transaction:
            account_info = f"На счет {mask_account_card(transaction['to'])}"

        if account_info:
            print(account_info)

        operation_amount = transaction.get('operationAmount', {})
        amount = operation_amount.get('amount', 'N/A')
        currency = operation_amount.get('currency', {}).get('code', 'N/A')
        print(f"Сумма: {amount} {currency}\n")

    # Пример использования count_operations_by_category
    categories_to_count = ['Перевод организации', 'Перевод со счета на счет', 'Перевод с карты на счет']
    operation_counts = count_operations_by_category(filtered_transactions, categories_to_count)
    print("Количество операций по категориям:")
    for category, count in operation_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
