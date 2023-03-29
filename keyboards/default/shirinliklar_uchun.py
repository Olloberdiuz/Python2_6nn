from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
shirinliklar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tort"),
            KeyboardButton(text="Perok")
        ],
        [
            KeyboardButton(text="Shokolat"),
            KeyboardButton(text="Rulet")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)