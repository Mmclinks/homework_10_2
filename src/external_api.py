import os
from typing import Any, Dict

import requests


def convert_amount_to_rubles(transaction: Dict[str, Any]) -> float:
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    if currency in ['USD', 'EUR']:
        api_key = os.getenv('EXCHANGE_API_KEY')
        response = requests.get(
            'https://api.apilayer.com/exchangerates_data/convert',
            headers={'apikey': api_key},
            params={'from': currency, 'to': 'RUB', 'amount': amount}
        )

        if response.status_code == 200:
            data = response.json()
            if 'result' in data:
                amount = data['result']
            else:
                raise ValueError(f'Exchange rate for {currency} not found in API response')
        else:
            raise ConnectionError(f'Failed to retrieve exchange rates from API, status code: {response.status_code}')

    return amount
