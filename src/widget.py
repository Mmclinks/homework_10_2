from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


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
            masked_number = get_mask_card_number(card_number)
            return f"{card_type} {masked_number}"
        else:
            return data


def get_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = dt.strftime("%d.%m.%Y")
    return formatted_date
