import os
import re
from pprint import pprint

import bs4
import requests
from bot.test_data import w, w2
from bot.utils.config import FOX_DIR, FOX_URL
from typing import List, Tuple
from bot.utils.helpers.Logger import logger





# Функция для поиска уникальных и неуникальных значений между двумя списками
def find_missing_entries(data1: List[str] | List, data2: List[str] | List) -> Tuple[List[str], List[str]]:
    # Проверка, что оба списка не пустые. Если один из них пустой, возвращаем второй список.
    if not data1 or not data2:
        return data1, data2

    # Преобразуем первый список в множество для быстрого поиска и исключения дубликатов
    data1_values = set(data1)

    # Преобразуем второй список в множество для быстрого поиска и исключения дубликатов
    data2_values = set(data2)

    # Находим уникальные элементы, которые есть только в data2, но отсутствуют в data1
    unique_values = data2_values - data1_values

    # Находим неуникальные элементы, которые присутствуют как в data1, так и в data2
    non_unique_values = data1_values & data2_values  # Используем пересечение множеств

    # Возвращаем результат в виде кортежа списков: (уникальные значения, неуникальные значения)
    return list(non_unique_values), list(unique_values)




# Функция для чтения изображения и получения его данных
def get_fox(fox_url = None):
    if fox_url is None:
        fox_url = FOX_URL
    # Запрос по URL
    response = requests.get(fox_url)

    # Проверка успешности запроса
    if response.status_code == 200:
        fox_image_url = response.json()['image']
    else:
        fox_image_url = os.path.join(FOX_DIR, 'fox_image.jpg')

    return fox_image_url


def parsing_job_card_():
    def get_text(tag: bs4.element.Tag):
        res = []
        tags = tag.contents

        for tag_item in tags:
            if not isinstance(tag_item, bs4.element.Tag):
                continue
            tags_item = tag_item.contents
            for tag_item2 in tags_item:
                tx = tag_item2.text
                if tx:
                    text_replaced = re.sub(r'\xa0', " ", tx)
                    text_replaced = re.sub(r'\xad|(-\s)*$', "", text_replaced)
                    res.append(text_replaced)
        return res

    def gets_tag_text(tag_article: bs4.element.Tag) -> List:

        res = []
        res.append(('Вакансия', tag_article.css.select('h1.page-title__title')[0].text))
        res.append(('Дата', tag_article.css.select('div.vacancy-header__date')[0].text))

        contents = tag_article.css.select('div.basic-section > div.content-section')
        for content in contents:
            h2 = content.select('h2')[0]
            list_content = h2.parent.find_next_sibling()
            res.append((h2.text, list_content.text))

        contents2 = tag_article.css.select('div.vacancy-description__text')
        tags = contents2[0].contents

        for item in range(1, len(tags), 2):
            res.append((tags[item - 1].text, get_text(tags[item])))
        return res
    return gets_tag_text



def request_():
    log = logger('request')
    def request(url) -> requests.Response:
        try:
            # Выполнение GET-запроса на указанный URL
            # Параметр timeout=15 устанавливает максимальное время ожидания ответа на запрос в 10 секунд
            response = requests.get(url, timeout=10)

            # Проверка успешности запроса (статус-код 200)
            # Если код ответа 4xx или 5xx, вызывается исключение HTTPError
            response.raise_for_status()
            return response

        except requests.exceptions.HTTPError as http_err:
            # Обработка HTTP ошибок (например, 404 или 500)
            # Критическая ошибка записывается в журнал и функция возвращает None
            log.critical(f"HTTP ошибка: {http_err}, url: {url}")


        except requests.exceptions.ConnectionError:
            # Обработка ошибок подключения (например, недоступность интернета)
            # Сообщение записывается в журнал, функция возвращает None
            log.critical("Ошибка подключения. Проверьте интернет-соединение. url: {url}")


        except requests.exceptions.Timeout:
            # Обработка ошибки таймаута, если запрос не завершен за 15 секунд
            # Сообщение записывается в журнал, функция возвращает None
            log.critical("Превышено время ожидания запроса.  url: {url}")

        except requests.exceptions.RequestException as err:
            # Обработка других исключений библиотеки requests
            # Сообщение записывается в журнал, функция возвращает None
            log.critical(f"Произошла ошибка: {err}, url: {url}")
        return None
    return request


def find_tag_text(tag: bs4.element.Tag, text: str) -> list[bs4.element.Tag | None]:
    # поиск элемента по текстовому содержимому
    res = [None]
    tags = tag.find_all(string=re.compile(text))
    if tags:
        res = [item.parent for item in tags]
    return res
# Экспорт
parsing_job_card = parsing_job_card_()
request = request_()

def pars_vacancies(url):
    '''
    Парсит карточку вакансии по url.
    :param url: Адрес карточки вакансии
    :return: Dist
    '''
    response = request(url)
    if  response is None:
        return None
    bs = bs4.BeautifulSoup(response.text, "lxml")
    res = parsing_job_card(bs.css.select("article.vacancy-show")[0])

    return res







