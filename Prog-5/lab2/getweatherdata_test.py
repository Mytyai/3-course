import pytest
from getweatherdata import get_weather_data
from owm_key import owm_api_key

# Тест для проверки возвращения None, если API ключ не передан
def test_without_key():
    assert get_weather_data("Moscow") is None, \
        "Для получения данных нужен api_key"

# Тест для проверки возвращения не None, если передан правильный API ключ и город
def test_valid_city_with_key():
    assert get_weather_data("Riga", api_key=owm_api_key) is not None, \
        "Не должно быть None при использовании ключа"

# Тест для проверки возвращения None для некорректного или пустого названия города
def test_invalid_city():
    assert get_weather_data("", api_key=owm_api_key) is None, \
        "Должно возвращать None для некорректного названия города"

# Тест для проверки возвращения словаря с корректной структурой данных
def test_response_structure():
    result = get_weather_data("Riga", api_key=owm_api_key)
    assert result is not None, "Должно быть None при корректных данных"
    assert isinstance(result, dict), "Должно быть словарём"
    assert "feels_like" in result, "Должно содержать ключ 'feels_like'"
    assert "country" in result, "Должно содержать ключ 'country'"

# Тест для проверки содержания правильного кода страны
@pytest.mark.parametrize("city, expected_country", [
    ("Chicago", "US"),
    ("Saint Petersburg", "RU"),
    ("Tokyo", "JP"),
])
def test_country_code(city, expected_country):
    result = get_weather_data(city, api_key=owm_api_key)
    assert result is not None, "Должно быть None"
    assert result.get("country") == expected_country, \
        f"Ожидалось, что страна будет '{expected_country}'"

# Тест для проверки содержания координат города с ключами 'lon' и 'lat'
@pytest.mark.parametrize("city", ["Chicago", "Saint Petersburg", "Tokyo"])
def test_coordinates_structure(city):
    result = get_weather_data(city, api_key=owm_api_key)
    assert result is not None, "Должно быть None"
    coords = result.get("coord")
    assert coords is not None, "Должно содержать координаты"
    assert "lon" in coords and "lat" in coords, "Координаты должны содержать 'lon' и 'lat'"
