from aiogram import types
from aiogram.types import ContentTypes

from loader import dp,bot,base


# Echo bot
menular = base.select_all_menu()



#
# @dp.message_handler(content_types=ContentTypes)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)

# @dp.message_handler()
# async def bot_echo(message: types.Message):
#     rasm_manzili = 'https://t.me/Soliyev_1_bot/3'
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Osh -- narxi  30 000 \n")
#
# @dp.message_handler(text="Kola")
# async def bot_echo(message: types.Message):
#     rasm_manzili = 'https://t.me/Soliyev_1_bot/4'
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Kol -- narxi  10 000 \n")