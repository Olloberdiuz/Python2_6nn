from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
ichimliklar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kola"),
            KeyboardButton(text="Fanta")
        ],
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Sharbat")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)