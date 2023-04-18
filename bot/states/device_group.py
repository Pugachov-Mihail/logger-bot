from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Device(StatesGroup):
    name = State()
    url = State()


class FindDevice(StatesGroup):
    name = State()