from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
ichimliklar_button2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kola2"),
            KeyboardButton(text="Fanta2")
        ],
        [
            KeyboardButton(text="Pepsi2"),
            KeyboardButton(text="Sharbat2")
        ],
        [
            KeyboardButton(text="Orqaga2")
        ]
    ],
    resize_keyboard=True
)