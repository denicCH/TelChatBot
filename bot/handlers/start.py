from aiogram import Router
from aiogram.types import Message  # Импортируем объект сообщения
from aiogram.filters import Command  # Импортируем фильтр для обработки команд (например, /start)


router = Router()

# Обработчик команды /start
@router.message(Command(commands=['start']))  # Указываем, что этот обработчик будет срабатывать на команду /start
async def send_welcome(message: Message):  # Определяем асинхронную функцию для обработки команды /start
    await message.answer("Привет! Спроси меня: 'какое сегодня число' или 'который час', и я скажу тебе.")
    # Отправляем приветственное сообщение пользователю, когда он введет команду /start