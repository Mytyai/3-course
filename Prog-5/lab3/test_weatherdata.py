import pytest
import json
from getweatherdata import get_weather_data

key = 'eb70f8184bae3104e3e4f5aa06282472'

def test_without_key():
    assert get_weather_data("Moscow") is None, \
        "ошибка: отсутствие api_key"
    
def test_without_params():
    assert get_weather_data('') is None, \
        "ошибка: отсуствие city и api_key"

def test_valid_city():
    assert get_weather_data("London", api_key=key) is not None, \
        "ошибка: неверно использован валидный ключ"

def test_type_of_res():
    assert get_weather_data("London", api_key=key) is None, \
        "ошибка: ожидался None"

def test_coords():
    get_weather_data('London', api_key=key)
    with open('data.json') as f:
        data = json.load(f)
    assert len(data.get('coord', {})) == 2, \
        "ошибка: отсутсвие долготы и широты (lon и lat)"

def test_feels_like():
    get_weather_data('London', api_key=key)
    with open('data.json') as f:
        data = json.load(f)
    assert isinstance(data.get('feels_like'), float), \
        "ошибка: feels_like должен быть float"

params = "city, api_key, expected_country"
params_countries = [
    ("Saint Petersburg", key, 'RU'),
    ("Tokyo", key, 'JP'),
    ("Las Vegas", key, 'US')
]

@pytest.mark.parametrize(params, params_countries)
def test_countries(city, api_key, expected_country):
    get_weather_data(city, api_key=key)
    with open('data.json') as f:
        data = json.load(f)
    assert data.get('country', 'NoValue') == expected_country, \
        "ошибка: неправильный код страны"