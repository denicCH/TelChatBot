import os
from bot.utils.config import DATA_BASE_DIR, PATH_TO_CACHE
import shelve
from bot.utils.helpers.Logger import logger
log = logger(name_loger = "Cache")

class Cache:
    def __init__(self, filename='database.db'):
        """
        Конструктор для инициализации базы данных (файла shelve) и кеша.
        :param filename: Имя файла базы данных
        """
        self.filename = os.path.join(DATA_BASE_DIR, filename)
        self._cache = {}  # Кеш для хранения данных в памяти
        self._load_cache()  # Загрузка данных в кеш при инициализации

    def _load_cache(self):
        """Загружает все данные из базы данных в кеш."""
        with shelve.open(self.filename) as db:
            self._cache = dict(db)  # Копируем данные в словарь кеша

    def _update_shelve(self, key, value=None, delete=False):
        """Обновляет базу данных shelve при изменении данных в кеше."""
        with shelve.open(self.filename, writeback=True) as db:
            if delete:
                del db[key]
            else:
                db[key] = value


    def read(self, key):
        """Читает запись из кеша."""
        if key not in self._cache:
            return None

        print(f"Прочитано из кеша: {key} -> {self._cache[key]}")
        return self._cache[key]

    def update(self, key, value):
        """Обновляет существующую запись в кеше и базе данных."""

        self._cache[key] = value  # Обновляем кеш
        self._update_shelve(key, value)  # Обновляем shelve
        print(f"Обновлено: {key} -> {value}")

    def delete(self, key):
        """Удаляет запись из кеша и базы данных."""
        if key not in self._cache:
            log.info(f"Ключ '{key}' не найден в кеше.")
            return None

        del self._cache[key]  # Удаляем из кеша
        self._update_shelve(key, delete=True)  # Удаляем из shelve
        print(f"Удалено: {key}")

    def list_all(self):
        """Выводит все записи в кеше."""
        print("Содержимое кеша:")
        for key, value in self._cache.items():
            print(f"{key} -> {value}")
        return self._cache


def init_cache(cache1:Cache) -> Cache:

    if  cache1.read('vacancys_all') is None:
        cache1.update('vacancys_all', {})

    if cache1.read('сache_url') is None:
        cache1.update('сache_url', {})

    if cache1.read('query') is None:
        cache1.update('query', {})

    return cache1


Cache = init_cache(Cache(os.path.join(PATH_TO_CACHE, 'cache')))


'''

vacancys_all = {
    "https://translate.google.com/details?hl=ru&sl=ru&tl=en&text=%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D1%8F&op=translate":
        {"time": '15:33', "vacancy": "содержимое вакансии 1"},
    "https://translate.google.com/de":
        {"time": '12:33', "vacancy": "содержимое вакансии 2"},
    "https://jobportal.com/vacancy/3":
        {"time": '09:45', "vacancy": "содержимое вакансии 3"},
    "https://jobportal.com/vacancy/4":
        {"time": '14:20', "vacancy": "содержимое вакансии 4"},
    "https://jobportal.com/vacancy/5":
        {"time": '10:15', "vacancy": "содержимое вакансии 5"},
    "https://jobportal.com/vacancy/6":
        {"time": '11:00', "vacancy": "содержимое вакансии 6"},
    "https://jobportal.com/vacancy/7":
        {"time": '13:45', "vacancy": "содержимое вакансии 7"},
    "https://jobportal.com/vacancy/8":
        {"time": '16:30', "vacancy": "содержимое вакансии 8"},
    "https://jobportal.com/vacancy/9":
        {"time": '08:15', "vacancy": "содержимое вакансии 9"},
    "https://jobportal.com/vacancy/10":
        {"time": '12:20', "vacancy": "содержимое вакансии 10"},
    "https://jobportal.com/vacancy/11":
        {"time": '10:30', "vacancy": "содержимое вакансии 11"},
    "https://jobportal.com/vacancy/12":
        {"time": '15:00', "vacancy": "содержимое вакансии 12"},
    "https://jobportal.com/vacancy/13":
        {"time": '11:20', "vacancy": "содержимое вакансии 13"},
    "https://jobportal.com/vacancy/14":
        {"time": '14:45', "vacancy": "содержимое вакансии 14"},
    "https://jobportal.com/vacancy/15":
        {"time": '09:30', "vacancy": "содержимое вакансии 15"},
    "https://jobportal.com/vacancy/16":
        {"time": '13:10', "vacancy": "содержимое вакансии 16"},
    "https://jobportal.com/vacancy/17":
        {"time": '15:40', "vacancy": "содержимое вакансии 17"},
    "https://jobportal.com/vacancy/18":
        {"time": '08:50', "vacancy": "содержимое вакансии 18"},
    "https://jobportal.com/vacancy/19":
        {"time": '10:05', "vacancy": "содержимое вакансии 19"},
    "https://jobportal.com/vacancy/20":
        {"time": '12:10', "vacancy": "содержимое вакансии 20"},
    "https://jobportal.com/vacancy/21":
        {"time": '11:55', "vacancy": "содержимое вакансии 21"},
    "https://jobportal.com/vacancy/22":
        {"time": '16:10', "vacancy": "содержимое вакансии 22"},
    "https://jobportal.com/vacancy/23":
        {"time": '09:05', "vacancy": "содержимое вакансии 23"},
    "https://jobportal.com/vacancy/24":
        {"time": '14:55', "vacancy": "содержимое вакансии 24"},
    "https://jobportal.com/vacancy/25":
        {"time": '13:25', "vacancy": "содержимое вакансии 25"},
}

query = {'строка запроса':{'time':"Время парсинга ссылок", 'ссылки':[]}}


vacancys_user = {'Содержит строку запроса': {
    { "dateTime":"Время парсинга ссылок",
      "entirety":False,
      "vacancys_links": [
                  "https://translate.google.com/details?hl=ru&sl=ru&tl=en&text=%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D1%8F&op=translate"
                , "https://aliexpress.ru/item/"
                , 'https://www.ozon.ru/category/televizory-15528'
                , 'https://vc.ru/midjourney/1135533-midjourney-v6-v-chem-otlichie-style-raw-ot-obychnoi-stilizacii'
      ]

     }
}
}
'''


"""
Написать функцию на вход которой подается строка запроса и idchat
1. функция анализирует наличее строки запроса  в кеше.
        если строка запроса есть, то:
                
                56654+
                
        если строки запроса нет, то:
            Начинаем процесс парсинга:
            1. Ф. проверяем,находим,  есть ли в базе вакансий данные о вакансиях соответствующие ссылкам, загруженные ранее.
            Часть данных соответствующих этим ссылкам будут возвращены и базы. Часть данных для которых не нашлось ссылок в базе
            будут парсится с сайта. 
        
                
На вход функции подается список ссылок, и параметр отвечающий за то, сколько за 1раз будет возвращено записей.
Необходимо возвращать по N записей содержащих ссылки и соответствующую вакансию.


"""



#
# def get_vacancies(link, links:List[str], n=3):
#     #
#     vacancys_links = сache.read('vacancys_all').keys()
#
#     res = find_missing_entries(vacancys_links, links)
#
#     return res
#
# res = get_vacancies('https://claude.ai', URLS)
