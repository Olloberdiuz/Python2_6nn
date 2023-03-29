from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_uchun import tasdiqlash_button, menu_button
from loader import dp, bot
from states.holatlar import Forma

# Echo bot
@dp.message_handler(text="Adminga Murojat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismingizni kiriting")
    await Forma.ism_qabul_qilish.set()


@dp.message_handler(state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await  state.update_data({'name':ism})
    await message.answer(text="Familyani kiriting")
    await Forma.familya_qabul_qilish.set()

@dp.message_handler(state=Forma.familya_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    familya = message.text
    await  state.update_data({'fam':familya})
    await message.answer(text="Yoshni kiriting")
    await Forma.yosh_qabul_qilish.set()

@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    age = message.text
    await  state.update_data({'yosh':age})
    await message.answer(text="Murojatni kiritin")
    await Forma.matn_qabul_qilish.set()

@dp.message_handler(state=Forma.matn_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    text = message.text
    await  state.update_data({'matn':text})
    malumot = await state.get_data()
    ismi = malumot.get("name")
    familyasi = malumot.get("fam")
    yoshi = malumot.get("yosh")
    matn = malumot.get("matn")
    s = f"Ism : {ismi} \n" \
        f"Familya : {familyasi} \n" \
        f"Yosh : {yoshi} \n" \
        f"Murojat : {matn} \n"
    await bot.send_message(chat_id=message.from_user.id,text=s,reply_markup=tasdiqlash_button)

    await Forma.tasdiqlash.set()

@dp.message_handler(state=Forma.tasdiqlash,text="Tasdiqlash")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text="Tasdiqlash", reply_markup=menu_button)
    await state.finish()

    malumot = await state.get_data()
    ismi = malumot.get("name")
    familyasi = malumot.get("fam")
    yoshi = malumot.get("yosh")
    matn = malumot.get("matn")
    s = f"Ism : {ismi} \n" \
        f"Familya : {familyasi} \n" \
        f"Yosh : {yoshi} \n" \
        f"Murojat : {matn} \n"
    await bot.send_message(chat_id=5186292191, text=s)
    await bot.send_message(chat_id=message.from_user.id, text="Adminga yuborildi")
    await state.finish()

@dp.message_handler(state=Forma.tasdiqlash,text="Bekor qilish")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Bekor qilindi",reply_markup=menu_button)
    await state.finish()