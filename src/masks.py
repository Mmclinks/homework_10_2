def get_mask_card_number(card_number):
    """Убедимся, что номер карты представлен строкой"""
    card_numbers = str(card_number)

    """Проверим, что длина номера карты допустима"""
    if len(card_numbers) < 16:
        raise ValueError("Номер карты слишком короткий.")

    """Формируем маскированную часть"""
    mask_part = card_number[6:-4].replace(card_number[6:-4], '*' * len(card_number[6:-4]))

    """Формируем итоговый маскированный номер"""
    mask_number = card_number[:6] + mask_part + card_number[-4:]

    """Разбиваем номер на блоки по 4 цифры и соединяем пробелами"""
    formatted_number = ' '.join([mask_number[i:i + 4] for i in range(0, len(mask_number), 4)])

    return formatted_number


def get_mask_account(account_num):
    """Преобразуем номер счета в строку, если он не является строкой"""
    account_number_str = str(account_num)
    """Получаем последние 4 цифры номера счета"""
    last_four_digits = account_number_str[-4:]
    """Формируем маску"""
    mask_account_number = "*" * (len(account_number_str) - 4) + last_four_digits
    return mask_account_number
