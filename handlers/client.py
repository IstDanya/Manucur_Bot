from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_client

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Приятного когтеточения)", reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Бот еще не знает о вас, познакомтесь с ним: \nhttps://t.me/ManucurBot')

# @dp.message_handler(commands=['Режим_работы'])
async def operating_mode(message : types.Message):
	await bot.send_message(message.from_user.id, "Когда Alexa нет дома")

# @dp.message_handler(commands=['Адрес'])
async def work_place(message : types.Message):
	await bot.send_location(message.from_user.id, 53.189686, 45.015740)



def register_handlers_user(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(operating_mode, commands=['Режим_работы'])
	dp.register_message_handler(work_place, commands=['Адрес'])
