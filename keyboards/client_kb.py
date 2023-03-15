from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Адрес')
b3 = KeyboardButton('/Masters_works')
b4 = KeyboardButton('/Контакты_мастера')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # замена клавиатуры на кнопки

kb_client.add(b1).add(b2).add(b3).add(b4)


