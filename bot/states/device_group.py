from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.dispatcher import FSMContext


class Device(StatesGroup):
    name = State()
    url = State()
    url_error = State()


class FindDevice(StatesGroup):
    name = State()


