import csv
import json
import logging
import os
import re
from collections import Counter
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


def read_transactions_from_xlsx(xlsx_file: str) -> List[Dict[str, Any]]:
    """
    Считывает транзакции из XLSX-файла и возвращает их в виде списка словарей.

    Каждый словарь представляет строку в XLSX-файле, где ключами являются заголовки столбцов,
    а значениями соответствующие значения ячеек.

    Args:
        xlsx_file (str): Имя XLSX-файла для считывания.

    Returns:
        List[Dict[str, Any]]: Список словарей, представляющих транзакции в XLSX-файле.
    """
    transactions: List[Dict[str, Any]] = []

    logger.debug("Попытка чтения XLSX-файла: %s", xlsx_file)
    try:
        workbook = openpyxl.load_workbook(xlsx_file)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            transaction = dict(zip(headers, row))

            # Преобразование даты в нужный формат
            if 'operationDate' in transaction:
                try:
                    transaction['operationDate'] = transaction['operationDate'].strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                except AttributeError:
                    pass  # Если дата уже строка в нужном формате

            # Преобразование суммы в нужный формат
            if 'operationAmount' in transaction:
                try:
                    transaction['operationAmount'] = float(transaction['operationAmount'])
                except ValueError:
                    pass  # Если не удалось преобразовать в число

            transactions.append(transaction)

        logger.debug("Успешно прочитан XLSX-файл: %s", xlsx_file)
    except FileNotFoundError:
        logger.error("Файл не найден: %s", xlsx_file)
    except Exception as e:
        logger.error("Ошибка при чтении XLSX-файла %s: %s", xlsx_file, e)

    return transactions


def count_operations_by_category(operations, categories):
    category_counts = Counter()
    for operation in operations:
        if operation['category'] in categories:
            category_counts[operation['category']] += 1
    return dict(category_counts)
