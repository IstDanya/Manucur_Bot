from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

import os 

# entry point
bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)


"""***************************USER PART***************************** """
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Приятного когтеточения)")
		await message.delete()
	except:
		await message.reply('Бот еще не знает о вас, познакомтесь с ним: \nhttps://t.me/ManucurBot')

@dp.message_handler(commands=['Режим_работы'])
async def operating_mode(message : types.Message):
	await bot.send_message(message.from_user.id, "Когда Alexa нет дома")

@dp.message_handler(commands=['Адрес'])
async def work_place(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Трудовиков 28')




"""***************************ADMIN PART**************************** """
"""***************************COMMON PART*************************** """

@dp.message_handler()
async def echo_send(message : types.Message):
	if message.text == "hi":
		await message.answer("Hello, Ich heise ManucurBot")
	
	




executor.start_polling(dp, skip_updates=True)
