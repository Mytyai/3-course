# Щеткин Дмитрий ИВТ 2.1
# Прог-5 Лабораторная работа 3. Создание своего пакета. Публикация на pypi

Перемещаю файл [getweatherdata.py](getweatherdata.py) в данный репозиторий из lab 2

Создаю [__init__.py](__init__.py)

Создаю [setup.py](setup.py) который будет содержать информацию для сборки и публикации пакета в PyPI

Команда для установки нужных инструментов:
```bash
pip install setuptools wheel twine
```

Команда для сборки:
```bash
python setup.py sdist bdist_wheel
```

Если сборка прошла успешно, в репозитории появятся папки dist, build и weatherdata_package_lr3.egg-info
![](photos/1.png)
![](photos/2.png)

Для публикации пакета на Test PyPI нужно зарегистрироваться на Test PyPI и получить API-токен для загрузки пакета.

Команда для загрузки на Test PyPI:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u __token__ -p <API-токен с Test PyPI>
```

При успешной загрузке пакета в терминале появится ссылка на загруженный пакет в Test PyPI:
![](photos/3.png)

Ссылка на загруженный пакет:
https://test.pypi.org/project/weatherdata-package-lr3/1.1.0/

