from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
fast_food_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Hotdog")
        ],
        [
            KeyboardButton(text="Pitsa"),
            KeyboardButton(text="Chizburger")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)