from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

eng_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Taomlar2"),
            KeyboardButton(text="Ichimliklar2")
        ],
        [
            KeyboardButton(text="Shirinliklar2"),
            KeyboardButton(text="Fast food2")
        ],
        [
            KeyboardButton(text="Kontakt2",request_contact=True),
            KeyboardButton(text="Lokatsiya2",request_location=True)
        ],
        [
            KeyboardButton(text="Orqaga2")
        ]
    ],
    resize_keyboard=True
)