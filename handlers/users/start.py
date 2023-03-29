from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.menu_uchun import menu_button
from keyboards.default.taomlar_uchun import taomlar_button
from keyboards.default.ichimliklar_uchun import ichimliklar_button
from keyboards.default.shirinliklar_uchun import shirinliklar_button
from keyboards.default.fast_food_uchun import fast_food_button
from keyboards.inline.tillar_uchun import tillar_buttons
from keyboards.default.eng_uchun import eng_button
from keyboards.default.taomlar_uchun2 import taomlar_button2
from keyboards.default.ichimliklar_uchun2 import ichimliklar_button2
from keyboards.default.shirinliklar_uchun2 import shirinliklar_button2
from keyboards.default.fast_food_uchun2 import fast_food_button2
from loader import dp, base, bot
from filters.shaxsiy_uchun import Shaxsiy


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ism,fam=fam,username=message.from_user.username,tg_id=user_id)
    except Exception:
        pass
    await message.answer(f"Assalomu Alekum Restoranmizga xush kelibsiz, {message.from_user.full_name}!",reply_markup=tillar_buttons)

# @dp.message_handler(text="Xurmatli mijoz mununi tanlang")
# async def bot_start(message: types.Message):
#     await message.answer(f"Assalomu alekum botga hush kelibsiz {message.from_user.full_name}!")

menular = base.select_all_menu()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    typee = message.text
    maxsulotlar = base.select_maxsulotlar(tur=typee)
    index = 0
    i = 0
    royxat = []
    for menu in maxsulotlar:
        # (1, 'Taomlar')
        if i % 2 == 0 and i != 0:
            index += 1
        if i % 2 == 0:
            royxat.append([KeyboardButton(text=menu[1])])
        else:
            royxat[index].append(KeyboardButton(text=menu[1]))
        i += 1
    royxat.append([KeyboardButton(text="Ortga")])
    maxsulot_button = ReplyKeyboardMarkup(keyboard=royxat, resize_keyboard=True)

    await message.answer(f"Maxsulotni tanlang",reply_markup=maxsulot_button)


menular = base.select_all_maxsulotlar()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    typee = message.text
    maxsulot = base.select_maxsulotlar(nomi=typee)[0]
    "(1, 'Osh', 30000, 'https://t.me/Soliyev_1_bot/3', None, 'Taomlar')"
    max_nomi = maxsulot[1]
    max_narxi = maxsulot[2]
    max_rasmi = maxsulot[3]
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=f"Nomi : {max_nomi}\n"
                                                                 f"Narxi : {max_narxi}\n"
                                                                 )




# @dp.message_handler(text="Ichimliklar")
# async def bot_start(message: types.Message):
#     await message.answer(f"Ichimlikni tanlang",reply_markup=ichimliklar_button)
#
# @dp.message_handler(text="Shirinliklar")
# async def bot_start(message: types.Message):
#     await message.answer(f"Shirinliklarni tanlang",reply_markup=shirinliklar_button)
#
# @dp.message_handler(text="Fast food")
# async def bot_start(message: types.Message):
#     await message.answer(f"Fast foodni tanlang",reply_markup=fast_food_button)
#
# @dp.message_handler(text="Orqaga")
# async def bot_start(message: types.Message):
#     await message.answer(f"Menuni tanlang",reply_markup=menu_button)
#
# @dp.callback_query_handler(text="til1")
# async def bot_start(xabar: CallbackQuery):
#     await xabar.message.answer(f"Menuni tanlang",reply_markup=menu_button)
#
# @dp.callback_query_handler(text="til2")
# async def bot_start(xabar: CallbackQuery):
#     await xabar.message.answer(f"Menuni tanlang",reply_markup=eng_button)
#
# @dp.message_handler(text="Taomlar2")
# async def bot_start(message: types.Message):
#     await message.answer(f"Taomlarni tanlang", reply_markup=taomlar_button2)
#
# @dp.message_handler(text="Ichimliklar2")
# async def bot_start(message: types.Message):
#     await message.answer(f"Ichimlikni tanlang",reply_markup=ichimliklar_button2)
#
# @dp.message_handler(text="Shirinliklar2")
# async def bot_start(message: types.Message):
#     await message.answer(f"Shirinliklarni tanlang",reply_markup=shirinliklar_button2)
#
# @dp.message_handler(text="Fast food2")
# async def bot_start(message: types.Message):
#     await message.answer(f"Fast foodni tanlang",reply_markup=fast_food_button2)
#
# @dp.message_handler(text="Orqaga2")
# async def bot_start(message: types.Message):
#     await message.answer(f"Menuni tanlang",reply_markup=eng_button)
#
# @dp.callback_query_handler(text="www")
# async def bot_start(xabar: CallbackQuery):
#     await xabar.message.answer(f"Qayta ishga tushirish",reply_markup=menu_button)
#
# @dp.message_handler(text="Ortga",)
# async def bot_start(message: types.Message):
#     await message.answer(text="Menu",reply_markup=menu_button)