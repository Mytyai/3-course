import re
import sys
import requests
from urllib.request import urlopen
from importlib.abc import PathEntryFinder, Loader
from importlib.util import spec_from_loader


class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available

    def find_spec(self, name, target=None):
        if name in self.available:
            origin = "{}/{}".format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin, is_package=True)
        else:
            return None


class URLLoader(Loader):
    def create_module(self, target):
        return None

    def exec_module(self, module):
        if module.__spec__.origin.endswith('/'):
            init_file_url = module.__spec__.origin + "__init__.py"
        else:
            init_file_url = module.__spec__.origin + "/__init__.py"
        
        with urlopen(init_file_url) as page:
            source = page.read()
        code = compile(source, init_file_url, mode="exec")
        exec(code, module.__dict__)


def url_hook(some_str):
    if not some_str.startswith(("http", "https")):
        raise ImportError
    
    try:
        response = requests.get(some_str)
        response.raise_for_status()
        data = response.text

    except requests.RequestException as e:
        print(f"Ошибка: Не удалось подключиться к хосту {some_str}. Причина: {e}")
        raise ImportError(f"Не удалось получить список модулей с {some_str}") from e

    filenames = re.findall("[a-zA-Z_][a-zA-Z0-9_]*/|[a-zA-Z_][a-zA-Z0-9_]*.py", data)
    modnames = {name[:-1] if name.endswith('/') else name[:-3] for name in filenames}
    return URLFinder(some_str, modnames)


sys.path_hooks.append(url_hook)
sys.path.append("http://localhost:8000")

import myremotepackage
myremotepackage.myfoo()
