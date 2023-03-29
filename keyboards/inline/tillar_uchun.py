from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data="til1"),
            InlineKeyboardButton(text="Ingiliz tili",callback_data="til2")
        ],
        [
            InlineKeyboardButton(text="Hamkorlarmiz", url="https://t.me/Soliyev_1_bot"),
            InlineKeyboardButton(text="Ulashish", switch_inline_query="Shu bot orqali bizdan maxsulot sotib olishingiz mumkun")
        ]
    ]
)