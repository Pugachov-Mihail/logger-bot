from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import device_crude
from bot.states import device_group

COMMAND_LIST = ["/start", "/add", "/edit", "/get_info"]


def find_value(func):
    async def validate(message: types.Message, state: FSMContext):
        if message.text == "" or message.text in COMMAND_LIST:
            await message.answer("Что бы прервать действие напиши: /reset", reply=False)
        else:
            await func(message, state)
    return validate


async def index(message: types.Message):
    await device_group.Device.name.set()
    await message.answer("Привет.\nЧто бы зарегистрировать API придумай ему имя.")


@find_value
async def create_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await device_group.Device.url.set()
    await message.answer("Введи URL с которого нужно получать всю историю логов:")


@find_value
async def create_url_device(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['url'] = message.text
    await device_group.Device.next()
    await message.answer("Введи URL с которого нужно получать ошибки:")


@find_value
async def create_url_error(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['url_error'] = message.text
    async with state.proxy() as data:
        name = data['name']
        url = data['url']
        url_error = data['url_error']
    await state.finish()

    if name == '' and url == '':
        await message.answer("Обмануть меня хочешь?")
    else:
        device = device_crude.create_device(name.upper())
        device_crude.create_url_device(url, device)
        device_crude.create_url_error(device, url_error)
        await message.answer("Сохранил.")


@find_value
async def get_info_find_name(message: types.Message):
    await device_group.FindDevice.name.set()
    await message.answer("Что бы получить информацию об API введи его имя:")


async def get_log_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    async with state.proxy() as data:
        name = data['name']

    current_device = device_crude.get_current_device(name.upper())
    await state.finish()
    if len(current_device) == 0:
        await message.answer("Дружок, мне кажется ты ошибся.")
    else:
        for url in current_device:
            await message.answer(f"ID URL: {url.id},\n"
                                 f"URL: {url.url}")


async def edit(message: types.Message):
    argument = message.get_args().split(" ")
    if len(argument) < 3:
        await message.answer("Для изменения URL устройства введи команду: \n "
                             "/edit <имя устройства> <ID url> <новый url>")
    else:
        name = argument[0]
        id = argument[1]
        url = argument[2]
        if device_crude.edit_url_device(name=name.upper(), id=id, url=url):
            await message.answer("Сохранил.")
        else:
            await message.answer("Парень, что то ты не так делаешь.")


async def reset_state(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Действие прервано")


async def unknown_command(message: types.Message):
    await message.answer("Не шали, шалунишка))))))")
