import pytest
import requests
from unittest.mock import patch
from main import CurrenciesList, ConcreteDecoratorJSON, ConcreteDecoratorCSV

# Тест для успешного запроса (HTTP 200)
def test_successful_get_currencies():
    currencies_list = CurrenciesList()
    try:
        result = currencies_list.get_currencies()
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed with error: {e}")

    assert isinstance(result, dict)
    assert 'USD' in result
    assert result['USD']['name'] == 'Доллар США'

# Тест для проверки ошибки 404
def test_404_error_handling():
    currencies_list = CurrenciesList()

    try:
        response = requests.get('http://www.cbr.ru/incorrect_url')
        response.raise_for_status()
        pytest.fail("Expected HTTPError but request succeeded")
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 404

# Тест для проверки сетевых ошибок
def test_connection_error_handling():
    currencies_list = CurrenciesList()

    try:
        response = requests.get('http://nonexistentwebsite.local')
        response.raise_for_status()
        pytest.fail("Expected ConnectionError but request succeeded")
    except requests.exceptions.ConnectionError:
        pass

# Тест метода get_currencies в классе CurrenciesList
def test_get_currencies():
    currencies_list = CurrenciesList()
    result = currencies_list.get_currencies()

    assert isinstance(result, dict)
    assert 'USD' in result
    assert result['USD']['name'] == 'Доллар США'

# Тест JSON декоратора
def test_decorator_json():
    json_decorator = ConcreteDecoratorJSON(CurrenciesList())
    result = json_decorator.get_currencies()

    assert isinstance(result, str)
    assert '"USD":' in result
    assert '"name": "Доллар США"' in result

# Тест CSV декоратора
def test_decorator_csv():
    csv_decorator = ConcreteDecoratorCSV(CurrenciesList())
    result = csv_decorator.get_currencies()

    assert isinstance(result, str)
    assert "EUR,Евро" in result
