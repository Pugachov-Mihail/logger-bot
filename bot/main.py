from aiogram import types
from aiogram.utils import executor


from config.config_db import Base, engine
from config.bot_config import dp
from handlers import logs
from states import device_group


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    dp.register_message_handler(logs.index, commands="start", state=None)
    dp.register_message_handler(logs.get_info_find_name, commands="get_info", state=None)
    dp.register_message_handler(logs.get_log_info, state=device_group.FindDevice.name)
    dp.register_message_handler(logs.create_name, state=device_group.Device.name)
    dp.register_message_handler(logs.create_url_device, state=device_group.Device.url)
    executor.start_polling(dp, skip_updates=True)


