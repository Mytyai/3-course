import json
import requests
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Dict, Any

# Абстрактный класс, задающий общий интерфейс для декораторов
class AbstractDecorator(ABC):
    @abstractmethod
    def get_currencies(self) -> Dict[str, Any]:
        pass

# Класс для получения списка валют с сайта ЦБ РФ
class CurrenciesList(AbstractDecorator):
    def get_currencies(self) -> Dict[str, Any]:
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        root = ET.fromstring(response.content)
        currencies = {}
        for valute in root.findall('Valute'):
            charcode = valute.find('CharCode').text
            name = valute.find('Name').text
            value = float(valute.find('Value').text.replace(',', '.'))
            nominal = int(valute.find('Nominal').text)
            currencies[charcode] = {'name': name, 'value': value, 'nominal': nominal}
        return currencies

# Декоратор для преобразования данных валют в JSON-формат
class ConcreteDecoratorJSON(AbstractDecorator):
    def __init__(self, component: AbstractDecorator):
        self._component = component

    def get_currencies(self) -> str:
        data = self._component.get_currencies()
        return json.dumps(data, indent=4, ensure_ascii=False)

# Декоратор для преобразования данных валют в CSV-формат
class ConcreteDecoratorCSV(AbstractDecorator):
    def __init__(self, component: AbstractDecorator):
        self._component = component

    def get_currencies(self) -> str:
        data = self._component.get_currencies()
        csv_data = "Currency,Name,Value,Nominal\n"
        for charcode, details in data.items():
            csv_data += f"{charcode},{details['name']},{details['value']},{details['nominal']}\n"
        return csv_data

if __name__ == "__main__":
    base = CurrenciesList()
    print("Словарь:")
    print(base.get_currencies())

    json_decorator = ConcreteDecoratorJSON(base)
    print("\nJSON:")
    print(json_decorator.get_currencies())

    csv_decorator = ConcreteDecoratorCSV(base)
    print("\nCSV:")
    print(csv_decorator.get_currencies())
