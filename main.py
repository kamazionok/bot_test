from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="5525609954:AAEpl8QluZhDn5bzPzhA4F8llHaceGRq7eU")
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Hello World!!!"
    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())
executor.start_polling(dp)

# I do not know all the operations. this work is done according to the tutorials
# I'm slowly analyzing all the actions of this code