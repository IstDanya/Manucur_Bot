from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Адрес')
b3 = KeyboardButton('Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # замена клавиатуры на кнопки

kb_client.add(b1).add(b2).add(b3)


