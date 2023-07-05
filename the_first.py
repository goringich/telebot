from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)
# the local site will not work
ur = 'https://goringich.github.io/telebot/'

@dp.message_handler(commands=["hello"])
async def start(message: types.Message):
    # return data only with Reply
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Open website", web_app=WebAppInfo(url=ur)))
    await message.answer("hello, my friend, the best", reply_markup=markup)

# data work
@dp.message_handler(content_types=["web_app_data"])
async def web_app(message: types.Message):
    res=json.loads(message.web_app_data.data)
    # formatted string
    
    name = res["name"]
    mail = res["mail"]
    phone = res["phone"]
    
    await message.reply("hi,men")
    await message.reply(f'Your name: {name}. Email: {mail}. Phone: {phone}')
    
@dp.message_handler(commands=["оплата","payment"])
async def payment(message: types.Message):
    # class aiogram.methods.send_invoice.SendInvoice(*, chat_id: Union[int, str], title: str, description: str, payload: str, provider_token: str, currency: str, prices: List[LabeledPrice], message_thread_id: Optional[int] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, start_parameter: Optional[str] = None, provider_data: Optional[str] = None, photo_url: Optional[str] = None, photo_size: Optional[int] = None, photo_width: Optional[int] = None, photo_height: Optional[int] = None, need_name: Optional[bool] = None, need_phone_number: Optional[bool] = None, need_email: Optional[bool] = None, need_shipping_address: Optional[bool] = None, send_phone_number_to_provider: Optional[bool] = None, send_email_to_provider: Optional[bool] = None, is_flexible: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = sentinel.UNSET_PROTECT_CONTENT, reply_to_message_id: Optional[int] = None, allow_sending_without_reply: Optional[bool] = None, reply_markup: Optional[InlineKeyboardMarkup] = None, **extra_data: Any)[source]
    await bot.send_invoice(message.chat.id, "Покупка рыбы", "Описание", "invoice", config.PAYMENT_TOKEN, "USD", [types.LabeledPrice("Покупка рыбы", 5 * 100 )])
    
    

executor.start_polling(dp)