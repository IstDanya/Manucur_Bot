from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
	print('Бот вышел в онлайн')
	sqlite_db.sql_start()

from handlers import client, admin, common

client.register_handlers_user(dp)
admin.register_handlers_admin(dp)
common.register_handlers_common(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
