import os
from typing import Dict

import requests


def convert_amount_to_rubles(transaction: Dict) -> float:
    amount = float(transaction['amount'])
    currency = transaction['currency']

    if currency in ['USD', 'EUR']:
        api_key = os.getenv('EXCHANGE_RATE_API_KEY')
        base_currency = 'RUB'
        response = requests.get(f'http://api.exchangeratesapi.io/latest?access_key={api_key}&symbols={currency},'
                                f'{base_currency}')

        if response.status_code == 200:
            data = response.json()
            if 'rates' in data and currency in data['rates']:
                exchange_rate = data['rates'][currency]
                amount *= exchange_rate
            else:
                raise ValueError(f'Exchange rate for {currency} not found in API response')
        else:
            raise ConnectionError(f'Failed to retrieve exchange rates from API, status code: {response.status_code}')

    return amount
