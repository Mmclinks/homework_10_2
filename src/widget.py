from masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(data: str) -> str:
    """Определяет тип маскировки и возвращает замаскированные данные."""
    if data.lower().startswith('счет'):
        # Обрабатываем счет
        parts = data.split(' ', 1)
        if len(parts) > 1:
            account_number = parts[1]
            masked_number = get_mask_account(account_number)
            return f"{parts[0]} {masked_number}"
        else:
            # Если номер счета не найден, возвращаем строку без изменений
            return data
    else:
        # Обрабатываем номер карты
        parts = data.rsplit(' ', 1)
        if len(parts) > 1:
            card_type = parts[0]
            card_number = parts[1]
            masked_number = get_mask_card_number(card_number)
            return f"{card_type} {masked_number}"
        else:
            # Если номер карты не найден, возвращаем строку без изменений
            return data


def get_date(date_str: str) -> str:
    """Разбирает строку в объект datetime и преобразует дату в нужный формат."""
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = dt.strftime("%d.%m.%Y")
    return formatted_date
