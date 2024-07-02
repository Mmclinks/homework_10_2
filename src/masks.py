def get_mask_card_number(card_number: str) -> str:
    """Убедимся, что номер карты представлен строкой"""
    card_numbers = str(card_number)

    """Проверим, что длина номера карты допустима"""
    if len(card_numbers) < 16:
        raise ValueError("Номер карты слишком короткий.")

    """Формируем маскированную часть"""
    mask_part = '*' * len(card_numbers[6:-4])

    """Формируем итоговый маскированный номер"""
    mask_number = card_numbers[:6] + mask_part + card_numbers[-4:]

    return mask_number


def get_mask_account(account_num: str) -> str:
    """Преобразуем номер счета в строку, если он не является строкой"""
    account_number_str = str(account_num)
    """Получаем последние 4 цифры номера счета"""
    last_four_digits = account_number_str[-4:]
    """Формируем маску"""
    mask_account_number = "*" * (len(account_number_str) - 4) + last_four_digits
    return mask_account_number
