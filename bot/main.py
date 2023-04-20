from aiogram.utils import executor

from config.config_db import Base, engine
from config.bot_config import dp, shutdown
from handlers import logs
from states import device_group


def main():
    Base.metadata.create_all(bind=engine)
    dp.register_message_handler(logs.index, commands=["start", "add"], state=None)
    dp.register_message_handler(logs.get_info_find_name, commands="get_info")
    dp.register_message_handler(logs.edit, commands="edit")
    dp.register_message_handler(logs.reset_state, commands="reset",
                                state=[device_group.FindDevice.name, device_group.Device.name, device_group.Device.url,
                                       device_group.Device.url_error])
    dp.register_message_handler(logs.get_logs_api, commands="history_log")
    dp.register_message_handler(logs.get_api_info, state=device_group.FindDevice.name)
    dp.register_message_handler(logs.get_name_find_log, state=device_group.FindLogsDevice.name)
    dp.register_message_handler(logs.create_name, state=device_group.Device.name)
    dp.register_message_handler(logs.create_url_device, state=device_group.Device.url)
    dp.register_message_handler(logs.create_url_error, state=device_group.Device.url_error)
    dp.register_message_handler(logs.unknown_command)


if __name__ == '__main__':
    main()
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
