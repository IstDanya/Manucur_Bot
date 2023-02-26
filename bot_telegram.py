from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

import os 

bot = Bot(token=os.environ['TOKEN'])

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
# @dp.message_handler()
async def echo_send(message : types.Message):
	await message.reply('Приветики, мб НОГОТОЧКИ?(метод reply, ответ на сообщение)')
	# await message.answer('Метод answer')
	await bot.send_message("ПНХ")
	# сделал modify




executor.start_polling(dp, skip_updates=True)
