from src.processing import filter_by_state, sort_by_date
from src.search import search_transactions_by_regex
from src.utils import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_xlsx


def main():
    csv_file = '/home/alex/Загрузки/transactions.csv'
    json_file = '/home/alex/Загрузки/operations.json'
    xlsx_file = '/home/alex/Загрузки/transactions_excel.xlsx'

    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Пользователь: ")

        if choice == '1':
            transactions = read_transactions_from_json(json_file)
            file_type = 'JSON'
        elif choice == '2':
            transactions = read_transactions_from_csv(csv_file)
            file_type = 'CSV'
        elif choice == '3':
            transactions = read_transactions_from_xlsx(xlsx_file)
            file_type = 'XLSX'
        else:
            print("Программа: Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")
            continue

        if not transactions:
            print(f"Программа: Ошибка при чтении {file_type}-файла. Попробуйте еще раз.")
            continue

        print(f"Программа: Для обработки выбран {file_type}-файл.")

        while True:
            status = input("Программа: Введите статус, по которому необходимо выполнить фильтрацию "
                           "(EXECUTED, CANCELED, PENDING): ").strip().upper()

            if status not in ['EXECUTED', 'CANCELED', 'PENDING']:
                print(f"Программа: Статус операции \"{status}\" недоступен.")
                continue
            else:
                print(f"Программа: Операции отфильтрованы по статусу \"{status}\".")
                break

        sorted_transactions = filter_by_state(transactions, state=status)

        sort_option = input("Программа: Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_option == 'да':
            ascending = input("Программа: Отсортировать по возрастанию или по убыванию? "
                              "По возрастанию/По убыванию: ").strip().lower()

            if ascending == 'по возрастанию':
                sorted_transactions = sort_by_date(sorted_transactions, ascending=True)
            elif ascending == 'по убыванию':
                sorted_transactions = sort_by_date(sorted_transactions, ascending=False)
            else:
                print("Программа: Неверный ввод. Операции будут отсортированы по умолчанию по возрастанию.")

        ruble_option = input("Программа: Выводить только рублевые тразакции? Да/Нет: ").strip().lower()
        if ruble_option == 'да':
            sorted_transactions = [transaction for transaction in sorted_transactions
                                   if transaction.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']

        search_option = input(
            "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
        if search_option == 'да':
            search_str = input("Программа: Введите строку для поиска: ").strip()
            sorted_transactions = search_transactions_by_regex(sorted_transactions, search_str)

        if not sorted_transactions:
            print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            print("Программа: Результаты обработки транзакций:")
            for transaction in sorted_transactions:
                print(f"Дата: {transaction.get('operationDate')}, Описание: {transaction.get('description')}, "
                      f"Сумма: {transaction.get('operationAmount', {}).get('amount')} "
                      f"{transaction.get('operationAmount', {}).get('currency', {}).get('code')}")

        repeat = input("Программа: Хотите выполнить еще одну операцию? Да/Нет: ").strip().lower()
        if repeat != 'да':
            print("Программа: Работа завершена. До свидания!")
            break

if __name__ == "__main__":
    main()
