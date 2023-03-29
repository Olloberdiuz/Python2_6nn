from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
fast_food_button2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lavash2"),
            KeyboardButton(text="Hotdog2")
        ],
        [
            KeyboardButton(text="Pitsa2"),
            KeyboardButton(text="Chizburger2")
        ],
        [
            KeyboardButton(text="Orqaga2")
        ]
    ],
    resize_keyboard=True
)