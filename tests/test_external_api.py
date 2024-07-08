import unittest
from unittest.mock import patch

from src.external_api import convert_amount_to_rubles


class TestConvertAmountToRubles(unittest.TestCase):

    @patch('os.getenv', return_value='dummy_api_key')
    @patch('requests.get')
    def test_convert_amount_usd_to_rub_success(self, mock_requests_get, mock_getenv):
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'result': 75.0}  # Пример успешного ответа от API

        transaction_usd = {
            'operationAmount': {
                'amount': '100',
                'currency': {
                    'code': 'USD'
                }
            }
        }

        converted_amount = convert_amount_to_rubles(transaction_usd)
        self.assertAlmostEqual(converted_amount, 75.0, places=2)

    @patch('os.getenv', return_value='dummy_api_key')
    @patch('requests.get')
    def test_convert_amount_eur_to_rub_success(self, mock_requests_get, mock_getenv):
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'result': 90.0}  # Пример успешного ответа от API

        transaction_eur = {
            'operationAmount': {
                'amount': '100',
                'currency': {
                    'code': 'EUR'
                }
            }
        }

        converted_amount = convert_amount_to_rubles(transaction_eur)
        self.assertAlmostEqual(converted_amount, 90.0, places=2)

    @patch('os.getenv', return_value='dummy_api_key')
    @patch('requests.get')
    def test_convert_amount_api_failure(self, mock_requests_get, mock_getenv):
        mock_requests_get.return_value.status_code = 404  # Ошибка соединения с API

        transaction_usd = {
            'operationAmount': {
                'amount': '100',
                'currency': {
                    'code': 'USD'
                }
            }
        }

        with self.assertRaises(ConnectionError):
            convert_amount_to_rubles(transaction_usd)

    @patch('os.getenv', return_value='dummy_api_key')
    @patch('requests.get')
    def test_convert_amount_value_error(self, mock_requests_get, mock_getenv):
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'rates': {'USD': 0.013, 'RUB': 1.0}}  # Ответ без 'result'

        transaction_usd = {
            'operationAmount': {
                'amount': '100',
                'currency': {
                    'code': 'USD'
                }
            }
        }

        with self.assertRaises(ValueError):
            convert_amount_to_rubles(transaction_usd)