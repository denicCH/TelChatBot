from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

class Url:
    def __init__(self, url):
        # Проверка, является ли переданная строка допустимым URL
        if not self.__is_url(url):
            raise ValueError(f"Переменная {url} не является URL")

        # Сохранение исходного URL
        self._url = url

        # Разбор URL на компоненты с использованием urlparse
        self._components_url = urlparse(url)

        # Парсинг строки запроса (query) в словарь
        self.query = parse_qs(self._components_url.query)

    def __is_url(self, url):
        """
        Вспомогательный метод для проверки, является ли строка допустимым URL.
        Проверяет наличие схемы (scheme) и сетевого местоположения (netloc).
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    @property
    def scheme(self):
        # Геттер для схемы (scheme) URL (например, http или https)
        return self._components_url.scheme

    @scheme.setter
    def scheme(self, value):
        # Сеттер для схемы, заменяющий текущую схему на новую
        self._components_url = self._components_url._replace(scheme=value)

    @property
    def netloc(self):
        # Геттер для сетевого местоположения (netloc) URL (например, example.com)
        return self._components_url.netloc

    @netloc.setter
    def netloc(self, value):
        # Сеттер для сетевого местоположения, заменяющий текущий netloc на новый
        self._components_url = self._components_url._replace(netloc=value)

    @property
    def path(self):
        # Геттер для пути (path) URL (например, /path/to/page)
        return self._components_url.path

    @path.setter
    def path(self, value):
        # Сеттер для пути, заменяющий текущий path на новый
        self._components_url = self._components_url._replace(path=value)

    @property
    def params(self):
        # Геттер для параметров (params) URL (например, параметры пути в некоторых схемах)
        return self._components_url.params

    @params.setter
    def params(self, value):
        # Сеттер для параметров, заменяющий текущий params на новый
        self._components_url = self._components_url._replace(params=value)

    def url(self):
        """
        Метод для получения полного URL.
        Собирает строку запроса (query) из параметров `self.query` и обновляет URL.
        """
        query_string = urlencode(self.query, doseq=True)  # Кодирует query в строку запроса
        self._components_url = self._components_url._replace(query=query_string)  # Обновляет query URL
        return urlunparse(self._components_url)  # Возвращает полный URL в виде строки

    def __str__(self):
        # Переопределение метода __str__, чтобы возвращать URL при преобразовании объекта в строку
        return self.url()
