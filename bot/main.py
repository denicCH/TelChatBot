# Запуск бота
import asyncio
from aiogram import Bot, Dispatcher, types, F  # Импортируем классы Bot, Dispatcher и типы данных (например, Message)
import sys
from aiogram.types import Message

from bot.handlers.common import logger
from bot.utils.config import BOT_TOKEN
from bot.handlers import common, start


if not (BOT_TOKEN is not None) or not BOT_TOKEN:
    logger.critical("Отсутствует BOT_TOKEN")
    sys.exit()

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)  # Инициализируем объект бота, передав ему токен
dp = Dispatcher()  # Инициализируем объект диспетчера, который будет управлять обработчиками



dp.include_router(start.router)
dp.include_router(common.router)


async def main():  # Главная асинхронная функция для запуска бота
    logger.info("Старт")
    await dp.start_polling(bot)  # Запускаем процесс поллинга (прослушивания новых сообщений)


    #



if __name__ == '__main__':  # Проверяем, что код запускается непосредственно, а не импортируется как модуль

    try:
        asyncio.run(main())  # Запуск основной функции
    except KeyboardInterrupt:
        logger.info("Программа завершена пользователем.")
