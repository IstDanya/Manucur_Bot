from create_bot import dp
from aiogram import types, Dispatcher
import json, string


# @dp.message_handler()
async def echo_send(message : types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('filthy_language.json')))) != set():
		await message.reply('Shut up clown!\n*cenzure*')
		await message.delete()

def register_handlers_common(dp : Dispatcher):
	dp.register_message_handler(echo_send)