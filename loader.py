import sqlite3
import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Создаем бота
bot = Bot(token=os.environ.get("API_TOKEN"), parse_mode=types.ParseMode.HTML)
# Создаем хранилище состояний
storage = MemoryStorage()
# Создаем диспетчер
dp = Dispatcher(bot, storage=storage)
# Создаем планировщик
scheduler = AsyncIOScheduler()

# Подключение к базе данных
connect = sqlite3.connect(os.environ.get("DATA"))
sql = connect.cursor()


