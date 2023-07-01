from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot("5460798180:AAEGrU8DD8NjlnyQAe7lVxVK-JwlZYRGGr0")
dp = Dispatcher(bot)
# the local site will not work
ur = 'https://goringich.github.io/telebot/'

@dp.message_handler(command=["hello!"])
async def start(message: types.Message):
    # return data only with Reply
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Open website", web_app=WebAppInfo(url=ur)))
    await message.answer("hello, my friend", reply_markup=markup)

# data work
@dp.message_handler(content_types=["web_app_data"])
async def web_app(message: types.Message):
    res=json.loads(message.web_app_data.data)
    # formatted string
    
    name = res["name"]
    email = res["email"]
    phone = res["phone"]
    
    await message.reply("hi,men")
    await message.reply(f'Your name: {name}. Email: {email}. Phone: {phone}')
    

executor.start_polling(dp)