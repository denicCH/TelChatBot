from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создание инлайн-кнопок
button1 = InlineKeyboardButton(text="Кнопка 1", callback_data="button1")
button2 = InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
button3 = InlineKeyboardButton(text="Кнопка 3", callback_data="button3")
button4 = InlineKeyboardButton(text="Кнопка 4", callback_data="button4")
button5 = InlineKeyboardButton(text="Кнопка 5", callback_data="button5")



# Создание инлайн-клавиатуры и добавление кнопок
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2, button3],
    [button4, button5]
],row_width=2)

# Теперь клавиатура корректно содержит кнопки


# inline_kb готова для использования при отправке сообщений
# Пример использования:
# await message.answer("Выберите одну из кнопок:", reply_markup=inline_kb)
