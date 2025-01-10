import os
import requests
import time
from xml.etree import ElementTree as ET
import matplotlib.pyplot as plt


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CurrencyRates(metaclass=SingletonMeta):
    def __init__(self, refresh_interval=1):
        self._currencies = {}
        self._last_update = 0
        self._refresh_interval = refresh_interval
        self._selected_currencies = []

    def _can_fetch(self):
        return (time.time() - self._last_update) >= self._refresh_interval

    def fetch_rates(self):
        if not self._can_fetch():
            raise Exception(f"Запрос можно делать не чаще, чем раз в {self._refresh_interval} сек.")

        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        root = ET.fromstring(response.content)
        valutes = root.findall("Valute")
        self._currencies = {}

        for valute in valutes:
            char_code = valute.find('CharCode').text
            name = valute.find('Name').text
            value = valute.find('Value').text
            nominal = int(valute.find('Nominal').text)

            value_int, value_frac = value.split(',')
            self._currencies[char_code] = {
                'name': name,
                'value': (value_int, value_frac),
                'nominal': nominal
            }

        self._last_update = time.time()

    def get_currency(self, char_code):
        return {char_code: None} if char_code not in self._currencies else {
            char_code: (self._currencies[char_code]['name'], f"{self._currencies[char_code]['value'][0]},{self._currencies[char_code]['value'][1]}")
        }

    def get_all_currencies(self):
        currencies_list = [
            {code: (data['name'], f"{data['value'][0]},{data['value'][1]}")}
            for code, data in self._currencies.items()
        ]
        formatted_output = "[\n" + ",\n ".join(str(item) for item in currencies_list) + "\n]"
        return formatted_output

    def set_selected_currencies(self, currencies):
        self._selected_currencies = currencies

    def visualize_currencies(self):
        if not self._currencies:
            raise Exception("Нет данных для визуализации.")

        currencies = self._selected_currencies or list(self._currencies.keys())
        values = [float(f'{self._currencies[code]["value"][0]}.{self._currencies[code]["value"][1]}')
                  for code in currencies]

        plt.figure(figsize=(10, 5))
        plt.bar(currencies, values)
        plt.title('Курсы валют по отношению к рублю')
        plt.xlabel('Валюта')
        plt.ylabel('Курс')

        file_path = os.path.join(os.path.dirname(__file__), 'currencies.jpg')
        plt.savefig(file_path)
        plt.show()

    def reset_last_update(self):
        self._last_update = 0

    def __del__(self):
        print("Удаление экземпляра CurrencyRates")


if __name__ == "__main__":
    cr = CurrencyRates()
    cr.fetch_rates()
    # Коды валют, которые вы хотите визуализировать, например: ['USD', 'EUR', 'GBP']
    cr.set_selected_currencies(['USD', 'EUR', 'GBP'])
    print(cr.get_all_currencies())
    cr.visualize_currencies()
