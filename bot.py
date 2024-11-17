from aiogram import Bot, Dispatcher, types  # Импортируем классы Bot, Dispatcher и типы данных (например, Message)
from aiogram.types import Message, Video  # Импортируем объект сообщения
from aiogram.filters import Command  # Импортируем фильтр для обработки команд (например, /start)
from aiogram import F  # Импортируем фильтры для работы с текстом сообщений
from datetime import datetime  # Импортируем модуль для работы с датой и временем
from bot.utils.config import *
from handlers import *
import asyncio


task: asyncio.Task = None


async def send_periodic_message():
    """
    Функция, которая отправляет сообщение в чат каждые 10 секунд.
    """
    while True:
        try:
            # Отправляем сообщение в указанный чат
            await bot.send_message(CHAT_ID, "Это периодическое сообщение!")
            logging.info("Сообщение отправлено успешно.")
        except Exception as e:
            logging.error(f"Ошибка при отправке сообщения: {e}")

        # Ждем 10 секунд перед следующей отправкой
        await asyncio.sleep(10)






# Логирование для отслеживания событий
logging.basicConfig(level=logging.INFO)  # Настраиваем базовое логирование для вывода информации уровня INFO

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)  # Инициализируем объект бота, передав ему токен
dp = Dispatcher()  # Инициализируем объект диспетчера, который будет управлять обработчиками


# Обработчик для приёма видео
@dp.message(F.video)
async def handle_video(message: types.Message):
    # Получаем файл видео
    video: Video|None = message.video  # Объект Video
    if not(video is not None):
        return
    file_id:str = video.file_id   # Получаем уникальный идентификатор файла
    file_name =  video.file_name if video.file_name is not None else file_id # Получаем имя video или присваеваем file_id
    file_size: int = video.file_size if video.file_size is not None else MAX_FILE_SIZE-1 # Размер файла
    logger.info(video)


    if file_size > MAX_FILE_SIZE:
        await message.answer("Извините, но размер файла превышает 20 МБ. Я не могу его обработать.")
        return


    # Загружаем файл с сервера Telegram
    file = await bot.get_file(file_id)  # Получаем объект File с путем к файлу на серверах Telegram
    if not(file.file_path is not None):
        logger.error("Путь к файлу на серверах Telegram отсутствует")
        return
    file_path:str = file.file_path # Путь к файлу на серверах Telegram



    # Создаем путь для сохранения видео
    file_name = f"downloads/{file_name}"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)  # Создаем директорию, если её нет

    # Скачиваем файл на локальный диск
    await bot.download_file(file_path, file_name)

    # Отправляем пользователю сообщение о том, что файл сохранён
    await message.answer(f"Видео принято и сохранено как {file_name}")




# Обработчик для приёма фотографии
@dp.message(F.photo)
async def handle_photo(message: types.Message):

    # Получаем фото с максимальным разрешением
    photo = message.photo[-1]  # Последняя фотография в списке - с наибольшим разрешением
    file_id = photo.file_id  # Получаем уникальный идентификатор файла
    file_n = message.caption or photo.file_id
    logger.info(message)
    # logger.info(file_name)
    # Создаем путь для сохранения изображения
    file_name = f"downloads/{file_n}.jpg"
    await message.bot.download(file=message.photo[-1].file_id, destination=file_name)


    # Загружаем файл с сервера Telegram
    file = await bot.get_file(file_id)  # Получаем объект File с путем к файлу на серверах Telegram
    file_path = file.file_path  # Путь к файлу на серверах Telegram



    os.makedirs(os.path.dirname(file_name), exist_ok=True)  # Создаем директорию, если её нет

    # Скачиваем файл на локальный диск
    await bot.download_file(file_path, file_name)

    # Отправляем пользователю сообщение о том, что файл сохранён
    await message.answer(f'Отлично, изображение сохранено как "{file_n}"')
    # await message.reply_photo('https://randomfox.ca/?i=24')











# Обработчик для приёма файла (документа)
@dp.message(F.document)
async def handle_document(message: Message):
    # Получаем файл (документ)
    document = message.document  # Объект Document
    file_id = document.file_id  # Получаем уникальный идентификатор файла
    file_name = document.file_name  # Имя файла
    file_size = document.file_size  # Размер файла
    logger.info(f'Размер файла {file_size}')


    # Проверяем, не превышает ли размер файла 20 МБ
    if file_size > MAX_FILE_SIZE:
        await message.answer("Извините, но размер файла превышает 20 МБ. Я не могу его обработать.")
        return

    try:
        # Загружаем файл с сервера Telegram
        file = await bot.get_file(file_id)  # Получаем объект File с путем к файлу на серверах Telegram
        file_path = file.file_path  # Путь к файлу на серверах Telegram

        # Создаем путь для сохранения файла
        save_path = f"downloads/{file_name}"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Создаем директорию, если её нет

        # Скачиваем файл на локальный диск
        await bot.download_file(file_path, save_path)

        # Отправляем пользователю сообщение о том, что файл сохранён
        await message.answer(f"Файл '{file_name}' принят и сохранён как {save_path}")

    except Exception as e:
        # Обрабатываем исключение и выводим его в лог
        await message.answer("Произошла ошибка при обработке файла.")
        logging.error(f"Ошибка при обработке файла {file_name}: {e}")



# Обработчик команды /start
@dp.message(Command(commands=['start']))  # Указываем, что этот обработчик будет срабатывать на команду /start
async def send_welcome(message: Message):  # Определяем асинхронную функцию для обработки команды /start
    await message.answer("Привет! Спроси меня: 'какое сегодня число' или 'который час', и я скажу тебе.")
    # Отправляем приветственное сообщение пользователю, когда он введет команду /start


# Обработчик команды /stop
@dp.message(Command(commands=['stop']))  # Указываем, что этот обработчик будет срабатывать на команду /start
async def send_welcome(message: Message):  # Определяем асинхронную функцию для обработки команды /stop
    task.cancel()
    await message.answer("Непрерывный ввод приостановлен")
    # Отправляем приветственное сообщение пользователю, когда он введет команду /start



# Обработчик текста для запроса даты
@dp.message(F.text.lower().contains('какое сегодня число'))  # Проверяем, содержит ли сообщение фразу 'какое сегодня число'
async def send_date(message: Message):  # Определяем асинхронную функцию для обработки сообщения
    today = datetime.now().strftime("%d.%m.%Y")  # Получаем текущую дату в формате дд.мм.гггг
    await message.answer(f"Сегодня {today}")  # Отправляем пользователю сообщение с текущей датой

# Обработчик текста для запроса времени
@dp.message(F.text.lower().contains('который час') | F.text.lower().contains('сколько время'))
# Проверяем, содержит ли сообщение фразы 'который час' или 'сколько время'
async def send_time(message: Message):  # Определяем асинхронную функцию для обработки запроса времени
    current_time = datetime.now().strftime("%H:%M")  # Получаем текущее время в формате чч:мм
    await message.answer(f"Сейчас {current_time}")  # Отправляем пользователю сообщение с текущим временем




# Обработчик любого текста (на случай, если запрос не про дату или время)
@dp.message()
async def echo_message(message: Message):  # Определяем асинхронную функцию для обработки текста
    # logging.info(f"{LogColors.OKGREEN}{message.text}{LogColors.ENDC}")
    logging.info(message.text)
    # await message.answer("Извините, я не понимаю этот запрос. Попробуйте спросить 'какое сегодня число' или 'который час'.")
    # Отправляем пользователю сообщение, что бот не понимает его запрос





# Запуск бота
async def main():  # Главная асинхронная функция для запуска бота
    global task
    task = asyncio.create_task(send_periodic_message())
    await dp.start_polling(bot)  # Запускаем процесс поллинга (прослушивания новых сообщений)
    send_periodic_message()
if __name__ == '__main__':  # Проверяем, что код запускается непосредственно, а не импортируется как модуль

    asyncio.run(main())  # Запускаем главную функцию для работы бота

