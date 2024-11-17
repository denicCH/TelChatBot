from aiogram import Router, types  # Импортируем классы Bot, Dispatcher и типы данных (например, Message)
from aiogram.types import Message  # Импортируем объект сообщения
from aiogram.filters import Command  # Импортируем фильтр для обработки команд (например, /start)
from aiogram import F  # Импортируем фильтры для работы с текстом сообщений
from datetime import datetime  # Импортируем модуль для работы с датой и временем
from bot.utils.config import *
from bot.utils.helpers.helpers import logger, get_fox
from bot.keyboards.Keyboard import kb1
from bot.keyboards.inline import inline_kb


logger= logger(name_loger = "chatbot")
router = Router()


@router.message(F.text.lower().contains('лису'))  # Проверяем, содержит ли сообщение фразу 'какое сегодня число'
async def send_1(message: Message):  # Определяем асинхронную функцию для обработки сообщения
    photo  = get_fox()
    await message.answer_photo(photo=photo)


@router.message(F.text.lower().contains('новая клавиатура'))  # Проверяем, содержит ли сообщение фразу 'какое сегодня число'
async def send_1(message: Message):  # Определяем асинхронную функцию для обработки сообщения
    await message.answer("Выберите одну из кнопок:", reply_markup=inline_kb)




# Обработчик текста для запроса даты
@router.message(F.text.lower().contains('сегодня число'))  # Проверяем, содержит ли сообщение фразу 'какое сегодня число'
async def send_date(message: Message):  # Определяем асинхронную функцию для обработки сообщения
    today = datetime.now().strftime("%d.%m.%Y")  # Получаем текущую дату в формате дд.мм.гггг
    await message.answer(f"Сегодня {today}")  # Отправляем пользователю сообщение с текущей датой

# Обработчик текста для запроса времени
@router.message(F.text.lower().contains('который час') | F.text.lower().contains('сколько время'))
# Проверяем, содержит ли сообщение фразы 'который час' или 'сколько время'
async def send_time(message: Message):  # Определяем асинхронную функцию для обработки запроса времени
    current_time = datetime.now().strftime("%H:%M")  # Получаем текущее время в формате чч:мм
    await message.answer(f"Сейчас {current_time}")  # Отправляем пользователю сообщение с текущим временем



# Обработчик любого текста (на случай, если запрос не про дату или время)
@router.message()
async def echo_message(message: Message):  # Определяем асинхронную функцию для обработки текста
    # logging.info(f"{LogColors.OKGREEN}{message.text}{LogColors.ENDC}")
    logger.info(message.text)
    # await message.answer("Извините, я не понимаю этот запрос. Попробуйте спросить 'какое сегодня число' или 'который час'.")
    # Отправляем пользователю сообщение, что бот не понимает его запрос
    # await message.answer("Выберите одну из кнопок:", reply_markup=inline_kb)
    # await message.answer("Выберите одну из кнопок:", reply_markup=reply_kb)
    # await message.answer("Выберите одну из кнопок:", reply_markup=kb1)



