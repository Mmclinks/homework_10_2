import logging
import os

# Создаем и настраиваем логгер
log_file = os.path.join(os.path.dirname(__file__), '..', 'logs', 'masks.log')
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('masks')


def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает маскированный номер карты, скрывая все, кроме первых 6 и последних 4 цифр.

    Args:
        card_number (str): Номер карты.

    Returns:
        str: Маскированный номер карты.

    Raises:
        ValueError: Если номер карты слишком короткий.
    """
    logger.debug("Маскировка номера карты: %s", card_number)
    card_num_str = str(card_number)  # Переименованная локальная переменная

    if len(card_num_str) < 16:
        logger.error("Номер карты слишком короткий: %s", card_number)
        raise ValueError("Номер карты слишком короткий.")

    mask_part = '*' * len(card_num_str[6:-4])
    mask_number = card_num_str[:6] + mask_part + card_num_str[-4:]

    logger.debug("Маскированный номер карты: %s", mask_number)
    return mask_number


def get_mask_account(account_num: str) -> str:
    """
    Возвращает маскированный номер счета, скрывая все, кроме последних 4 цифр.

    Args:
        account_num (str): Номер счета.

    Returns:
        str: Маскированный номер счета.
    """
    logger.debug("Маскировка номера счета: %s", account_num)
    account_num_str = str(account_num)  # Переименованная локальная переменная
    last_four_digits = account_num_str[-4:]
    mask_account_number = "*" * (len(account_num_str) - 4) + last_four_digits

    logger.debug("Маскированный номер счета: %s", mask_account_number)
    return mask_account_number


# Пример вызова функций
# if __name__ == "__main__":
#     card_num = "1234567812345678"
#     masked_card = get_mask_card_number(card_num)
#     print(f"Маскированный номер карты: {masked_card}")
#
#     account_num = "12345678"
#     masked_account = get_mask_account(account_num)
#     print(f"Маскированный номер счета: {masked_account}")
