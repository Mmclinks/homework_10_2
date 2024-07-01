# test_external_api.py

import unittest
from unittest.mock import MagicMock, patch

from src.external_api import convert_amount_to_rubles


class TestConvertAmountToRubles(unittest.TestCase):

    @patch('requests.get')
    @patch('os.getenv')
    def test_convert_amount_usd_to_rub_success(self, mock_getenv, mock_requests_get):
        # Устанавливаем мок для os.getenv
        mock_getenv.return_value = 'dummy_api_key'

        # Устанавливаем мок для requests.get
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'rates': {'USD': 0.013, 'RUB': 1.0}}

        # Тестирование конвертации USD в RUB
        transaction_usd = {'amount': '100', 'currency': 'USD'}
        converted_amount_usd = convert_amount_to_rubles(transaction_usd)
        self.assertAlmostEqual(converted_amount_usd, 1.3, places=2)

    @patch('requests.get')
    @patch('os.getenv')
    def test_convert_amount_eur_to_rub_success(self, mock_getenv, mock_requests_get):
        # Устанавливаем мок для os.getenv
        mock_getenv.return_value = 'dummy_api_key'

        # Устанавливаем мок для requests.get
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'rates': {'EUR': 0.012, 'RUB': 1.0}}

        # Тестирование конвертации EUR в RUB
        transaction_eur = {'amount': '100', 'currency': 'EUR'}
        converted_amount_eur = convert_amount_to_rubles(transaction_eur)
        self.assertAlmostEqual(converted_amount_eur, 1.2, places=2)

    @patch('requests.get')
    @patch('os.getenv')
    def test_convert_amount_non_supported_currency(self, mock_getenv, mock_requests_get):
        # Устанавливаем мок для os.getenv
        mock_getenv.return_value = 'dummy_api_key'

        # Устанавливаем мок для requests.get
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {'rates': {'RUB': 1.0}}

        # Тестирование для валюты, не поддерживаемой API
        transaction_invalid = {'amount': '100', 'currency': 'XYZ'}
        converted_amount_invalid = convert_amount_to_rubles(transaction_invalid)
        self.assertEqual(converted_amount_invalid, 100.0)

    @patch('requests.get')
    @patch('os.getenv')
    def test_convert_amount_api_failure(self, mock_getenv, mock_requests_get):
        # Устанавливаем мок для os.getenv
        mock_getenv.return_value = 'dummy_api_key'

        # Устанавливаем мок для requests.get с ошибочным статусом
        mock_requests_get.return_value.status_code = 404

        # Тестирование обработки ошибки при получении данных от API
        transaction_usd = {'amount': '100', 'currency': 'USD'}
        with self.assertRaises(ConnectionError):
            convert_amount_to_rubles(transaction_usd)
