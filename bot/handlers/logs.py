from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.config_db import session

from bot.models import device_crude
from bot.states import device_group


async def index(message: types.Message):
    await device_group.Device.name.set()
    await message.answer("Привет. Что бы зарегистрировать новое устройтво придумай ему имя.")


async def create_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await device_group.Device.next()
    await message.answer("Введи URL с которого нужно получать логи")


async def create_url_device(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['url'] = message.text

    async with state.proxy() as data:
        name = data['name']
        url = data['url']

    device = device_crude.create_device(name)
    device_crude.create_url_device(url, device)

    await state.finish()
    await message.answer("Сохранил")


async def get_info_find_name(message: types.Message):
    await device_group.FindDevice.name.set()
    await message.answer("Что бы получить информацию по боту введи его имя")


async def get_log_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    async with state.proxy() as data:
        name = data['name']
    current_device = device_crude.get_current_device(name)
    await state.finish()
    await message.answer(current_device.url_devices)
