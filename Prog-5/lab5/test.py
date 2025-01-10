import pytest
from main import CurrencyRates

# Тест для проверки неправильного кода валюты
def test_invalid_currency():
    cr = CurrencyRates()
    cr.fetch_rates()
    assert cr.get_currency('R9999') == {'R9999': None}

# Тест для проверки корректного кода валюты и названия валюты
def test_valid_currency_name():
    cr = CurrencyRates(refresh_interval=0)
    cr.reset_last_update()
    cr.fetch_rates()
    result = cr.get_currency('GBP')['GBP']
    assert isinstance(result, tuple)
    assert result[0] == 'Фунт стерлингов'

# Тест для проверки диапазона значений валюты
def test_valid_currency_value():
    cr = CurrencyRates(refresh_interval=0)
    cr.reset_last_update()
    cr.fetch_rates()
    result = cr.get_currency('GBP')['GBP']
    value = float(f'{result[1].replace(",", ".")}')
    assert 0 < value < 999
