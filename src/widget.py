from masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Определим тип маскировки"""
    if data.lower().startswith('счет'):
        """Обрабатываем счет"""
        parts = data.split(' ', 1)
        if len(parts) > 1:
            account_number = parts[1]
            masked_number = get_mask_account(account_number)
            return f"{parts[0]} {masked_number}"
        else:
            """Если номер счета не найден, возвращаем строку без изменений"""
            return data

    else:
        """Обрабатываем номер карты"""
        parts = data.rsplit(' ', 1)
        if len(parts) > 1:
            card_type = parts[0]
            card_number = parts[1]
            masked_number = get_mask_card_number(card_number)
            return f"{card_type} {masked_number}"
        else:
            """Если номер карты не найден, возвращаем строку без изменений"""
            return data

# пример ввода
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Счет 64686473678894779589"))
