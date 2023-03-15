from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_client
from data_base import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

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
async def address(message : types.Message):
	await bot.send_location(message.from_user.id, 54.712686, 20.543004)
	await bot.send_message(message.from_user.id,  'Физкультурная 25, 4-й подъезд')


# @dp.message_handler(commands=['Меню'])
async def manic_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)

@dp.message_handler(commands=['Контакты_мастера'])
async def contacts(message : types.Message):
	await message.answer('Контакты:' + emoji.emojize(':telephone:'), reply_markup=urlkb)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='VK' , url = 'https://vk.com/ulianalezhnina')
urlkb.add(urlButton)


def register_handlers_user(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(operating_mode, commands=['Режим_работы'])
	dp.register_message_handler(address, commands=['Адрес'])
	dp.register_message_handler(manic_menu_command, commands=['Masters_works'])
