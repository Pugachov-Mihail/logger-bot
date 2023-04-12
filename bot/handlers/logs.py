from aiogram import types
from sqlalchemy.orm import Session

from bot.models.device_crude import create_device_and_url


async def index(message: types.Message):
    await message.answer("Привет. Что бы зарегистрировать новое устройтво придумай ему имя.")


async def create_device(message: types.Message):
    name = message.text
    a = create_device_and_url(name)
    await message.answer(a)