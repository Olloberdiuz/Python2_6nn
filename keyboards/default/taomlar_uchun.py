from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
taomlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="lagmon")
        ],
        [
            KeyboardButton(text="Shorva"),
            KeyboardButton(text="Kabob")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)