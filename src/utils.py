import csv
import json
import logging
import os
from typing import Any, Dict, List

import openpyxl

# Создаем и настраиваем логгер
log_file = os.path.join(os.path.dirname(__file__), '..', 'logs', 'utils.log')
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('utils')


def read_transactions_from_json(json_file_path: str) -> List[Dict[str, Any]]:
    """
    Читает транзакции из JSON-файла и возвращает их в виде списка словарей.

    Args:
        json_file_path (str): Путь к JSON-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций, если файл корректный. Пустой список в случае ошибки.
    """
    logger.debug("Попытка чтения JSON-файла: %s", json_file_path)
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.debug("Успешно прочитан JSON-файл: %s", json_file_path)
                return data
            else:
                logger.error("Неверный формат данных в файле: %s", json_file_path)
                return []
    except FileNotFoundError:
        logger.error("Файл не найден: %s", json_file_path)
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON в файле: %s", json_file_path)
        return []


def read_transactions_from_csv(file_name: str) -> List[Dict[str, str]]:
    """
    Считывает транзакции из CSV-файла и возвращает их в виде списка словарей.

    Каждый словарь представляет строку в CSV-файле, где ключами являются заголовки столбцов,
    а значениями соответствующие значения ячеек.

    Аргументы:
        file_name (str): Имя CSV-файла для считывания.

    Возвращает:
        List[Dict[str, str]]: Список словарей, представляющих транзакции в CSV-файле.
    """
    transactions: List[Dict[str, str]] = []
    current_dir = os.path.dirname(__file__)  # Получаем текущий каталог скрипта
    file_path = os.path.join(current_dir, file_name)  # Формируем полный путь к файлу

    logger.debug("Попытка чтения CSV-файла: %s", file_path)
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(dict(row))
        logger.debug("Успешно прочитан CSV-файл: %s", file_path)
    except FileNotFoundError:
        logger.error("Файл не найден: %s", file_path)
    except Exception as e:
        logger.error("Ошибка при чтении CSV-файла %s: %s", file_path, e)

    return transactions


def read_transactions_from_xlsx(xlsx_file: str) -> List[Dict[str, str]]:
    """
    Считывает транзакции из XLSX-файла и возвращает их в виде списка словарей.

    Каждый словарь представляет строку в XLSX-файле, где ключами являются заголовки столбцов,
    а значениями соответствующие значения ячеек.

    Аргументы:
        xlsx_file (str): Имя XLSX-файла для считывания.

    Возвращает:
        List[Dict[str, str]]: Список словарей, представляющих транзакции в XLSX-файле.
    """
    transactions: List[Dict[str, str]] = []

    logger.debug("Попытка чтения XLSX-файла: %s", xlsx_file)
    try:
        workbook = openpyxl.load_workbook(xlsx_file)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            transactions.append(dict(zip(headers, row)))
        logger.debug("Успешно прочитан XLSX-файл: %s", xlsx_file)
    except FileNotFoundError:
        logger.error("Файл не найден: %s", xlsx_file)
    except Exception as e:
        logger.error("Ошибка при чтении XLSX-файла %s: %s", xlsx_file, e)

    return transactions


# В других частях проекта, где нужно считать данные из CSV
# или XLSX файлов, импортировать эти функции следующим образом:
#
# from utils import read_transactions_from_csv, read_transactions_from_xlsx
#
# # Пример использования для CSV
# csv_file = '/home/alex/Загрузки/transactions.csv'
# csv_transactions = read_transactions_from_csv(csv_file)
# print(csv_transactions)
#
# # Пример использования для XLSX
# xlsx_file = '/home/alex/Загрузки/transactions_excel.xlsx'
# xlsx_transactions = read_transactions_from_xlsx(xlsx_file)
# print(xlsx_transactions)


def count_operations_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """
    Функция подсчитывает количество операций в каждой категории на основе описания транзакций.

    Args:
    - transactions (List[Dict[str, str]]): Список словарей с данными о банковских операциях.
      Каждый словарь должен содержать поле 'description', описывающее операцию.
    - categories (List[str]): Список категорий операций.

    Returns:
    - Dict[str, int]: Словарь, где ключи — названия категорий, а значения — количество операций в каждой категории.
    """
    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get('description', '')

        for category in categories:
            if category.lower() in description.lower():
                category_counts[category] += 1
                break

    return category_counts
