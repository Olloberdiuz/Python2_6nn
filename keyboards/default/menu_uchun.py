from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import base

menular = base.select_all_menu()
index =0
i = 0
royxat = []

for menu in menular:
    # (1, 'Taomlar')
    if i%2==0 and i  !=0:
        index+=1
    if i%2==0:
        royxat.append([KeyboardButton(text=menu[1])])
    else:
        royxat[index].append(KeyboardButton(text=menu[1]))
    i+=1

menu_button = ReplyKeyboardMarkup(keyboard=royxat,resize_keyboard=True)


tasdiqlash_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")

        ],
        [
            KeyboardButton(text="Kontakt2", request_contact=True),
            KeyboardButton(text="Lokatsiya2", request_location=True)
        ]
    ],
    resize_keyboard=True
)