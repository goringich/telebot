from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot("5460798180:AAEGrU8DD8NjlnyQAe7lVxVK-JwlZYRGGr0")
dp = Dispatcher(bot)
# the local site will not work
ur = 'https://goringich.github.io/telebot/index.html'

@dp.message_handler()
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Open website", web_app=WebAppInfo(url=ur)))
    await message.answer("hello, my friend", reply_markup=markup)

executor.start_polling(dp)