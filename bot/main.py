from aiogram import types
from aiogram.utils import executor

from config.config_db import Base, engine
from config.bot_config import dp
from handlers import logs


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    dp.register_message_handler(logs.index, commands="start")
    dp.register_message_handler(logs.create_device)
    executor.start_polling(dp, skip_updates=True)


