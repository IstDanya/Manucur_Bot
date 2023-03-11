from aiogram import Bot, Dispatcher
import os

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)