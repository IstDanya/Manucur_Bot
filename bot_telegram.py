from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
	print('Бот вышел в онлайн')

from handlers import user, admin, common

user.register_handlers_user(dp)
common.register_handlers_common(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
