# import json
# from typing import Any, Dict, List
#
#
# def read_transactions_from_json(json_file_path: str) -> List[Dict[str, Any]]:
#     try:
#         with open(json_file_path, 'r') as file:
#             data = json.load(file)
#             if isinstance(data, list):
#                 return data
#             else:
#                 return []
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []
import json
import logging
import os
from typing import Any, Dict, List

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
