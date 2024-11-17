import logging
import os
import sys
import colorlog
from bot.utils.config import LOGS_DIR


def logger(name_loger=""):
    # Создание логгера
    logger = colorlog.getLogger(name_loger)
    logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень логгера

    # Создание обработчика для записи логов в файл с кодировкой UTF-8
    file_handler = logging.FileHandler(os.path.join(LOGS_DIR, 'bot.log'), encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)  # Устанавливаем уровень для файла

    # Создание обработчика для вывода логов в консоль с цветами
    console_handler = colorlog.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # Устанавливаем уровень для консоли
    console_handler.setFormatter(colorlog.ColoredFormatter(
        "%(filename)s:%(lineno)d: %(name)s - %(asctime)s - %(log_color)s%(levelname)s: %(message)s",
        # Цвет текста и уровень логирования
        log_colors={
            'DEBUG': 'blue',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    ))

    # Настройка формата логирования для файла
    formatter = logging.Formatter("%(filename)s:%(lineno)d: %(name)s - %(asctime)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(formatter)

    # Добавление обработчиков к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger