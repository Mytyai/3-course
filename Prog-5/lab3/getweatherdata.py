import json
from requests import get

def get_weather_data(place, api_key=None):
    with get(
            f'https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={api_key}'
    ) as f:
        res = f.text

        res_json = json.loads(res)

    res_json = {
        'name' : res_json['name'],
        'country' : res_json['sys']['country'],
        'coord' : res_json['coord'],
        'feels_like' : res_json['main']['feels_like'],
        'humidity' : res_json['main']['humidity'],
        'pressure' : res_json['main']['pressure'],
        'speed_wind' : res_json['wind']['speed'],
    }

    with open('data.json', 'w') as f:
        json.dump(res_json, f, ensure_ascii=False, indent=4)

    print(res_json)