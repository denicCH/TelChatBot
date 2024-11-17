from dotenv import dotenv_values
import os
from pathlib import Path

env_values = dotenv_values()

# Определение пути к корню проекта
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PATH_TO_CACHE = os.path.join(BASE_DIR, 'data')
BOT_TOKEN = env_values.get("BOT_TOKEN")  # Укажи здесь токен, полученный от BotFather
# Максимальный размер файла (20 МБ)
MAX_FILE_SIZE = 20 * 1024 * 1024
CHAT_ID = env_values.get("CHAT_ID")
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
FOX_DIR = PATH_TO_CACHE
FOX_URL = r"https://randomfox.ca/floof/"
BASE_URL = r'https://career.habr.com'
DATA_BASE_DIR = os.path.join(BASE_DIR, 'data')
LIFETIME_LINKS = 60 # Указывается в минутах

print("Путь к корню проекта:", BASE_DIR)

