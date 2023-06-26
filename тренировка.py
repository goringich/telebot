# from aiogram import Bot, Dispatcher, executor, types
#
# bot = Bot("5460798180:AAEGrU8DD8NjlnyQAe7lVxVK-JwlZYRGGr0")
# dp = Dispatcher(bot)
# u = "https://vk.com/evlampiy1"

#
# # images
# @dp.message_handler(content_types=["photo"])
# async def img(message: types.Message):
#     file = open("assets/1619258253_6-phonoteka_org-p-flag-rf-fon-7.jpg", "rb")
#     await message.answer_photo(file)
#
# # texts
# @dp.message_handler(commands=["hello"])
# async def mess(message: types.Message):
#     # send message
#     # await bot.send_message(message.chat.id,"hello")
#     # more convenient
#     #  await message.answer("Hello")
#
#     # answer, reply
#     await message.reply("hi,men")
#
#
# # call up callback function, url in inline button
# @dp.message_handler(commands=["inline", "button"])
# async def info(message: types.Message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Site", url=u))
#     markup.add(types.InlineKeyboardButton("Ask the question", callback_data="ask!"))
#     await message.reply("hello", reply_markup=markup)
#
# # callback function
# @dp.callback_query_handler()
# async def callback(call):
#     await call.message.answer(call.data)
#
# # button will abyss after the click
# @dp.message_handler(commands=["reply"])
# async def reply(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     markup.add(types.KeyboardButton("Ого!"))
#     markup.add(types.KeyboardButton("Site"))
#     await message.answer("Bye, bye!", reply_markup=markup)
#
# executor.start_polling(dp)
