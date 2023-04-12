import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher


load_dotenv()

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
