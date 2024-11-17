from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание кнопок
button1 = KeyboardButton(text="Кнопка 1")
button2 = KeyboardButton(text="Кнопка 2")
button3 = KeyboardButton(text="Кнопка 3")
button4 = KeyboardButton(text="Кнопка 4")
button5 = KeyboardButton(text="Кнопка 5")

# Создание клавиатуры и добавление кнопок
reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [button1], [button2], [button3], [button4], [button5]
])

# Пример использования:
# await message.answer("Выберите одну из кнопок:", reply_markup=reply_kb)