from aiogram import types

button1 = types.KeyboardButton(text="/start")
button2 = types.KeyboardButton(text="Который час")
button3 = types.KeyboardButton(text="Kакое сегодня число")
button4 = types.KeyboardButton(text="Покажи лису")
button5 = types.KeyboardButton(text="Закрыть")
button6 = types.KeyboardButton(text="Новая клавиатура", callback_data="new_keyboard")

keyboard1 = [
    [button1, button2, button3],
    [ button4,button6, button5],
]


keyboard2 = [
    [button3, button5],
    [ button4, button1],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2,resize_keyboard=True)