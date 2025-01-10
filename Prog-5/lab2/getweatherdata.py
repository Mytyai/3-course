import json
from requests import get

def get_weather_data(place, api_key=None):
    if not api_key:
        print("API ключ не задан.")
        return None
    
    response = get(
        f'https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={api_key}'
    )

    if response.status_code != 200:
        print(f"Ошибка запроса: {response.status_code}")
        return None
    
    res_json = response.json()

    if 'name' not in res_json:
        return None

    res_json = {
        'name': res_json['name'],
        'country': res_json['sys']['country'],
        'coord': res_json['coord'],
        'feels_like': res_json['main']['feels_like'],
        'humidity': res_json['main']['humidity'],
        'pressure': res_json['main']['pressure'],
        'speed_wind': res_json['wind']['speed'],
    }

    with open('data.json', 'w') as f:
        json.dump(res_json, f, ensure_ascii=False, indent=4)

    print(res_json)

    return res_json
