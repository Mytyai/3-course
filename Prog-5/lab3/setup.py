from setuptools import setup, find_packages

setup(
    name="weatherdata_package_lr3",
    version="1.1.0",
    author="Mityai",
    author_email="shetkindima@yandex.ru",
    description="A package to fetch weather data using OpenWeatherMap API",
    long_description=open('readme.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mytyai/3-course/tree/master/Prog-5/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests",
        'pytest'
    ],
)