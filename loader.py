import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import API_TOKEN, database

from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Создаем бота
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
# Создаем хранилище состояний
storage = MemoryStorage()
# Создаем диспетчер
dp = Dispatcher(bot, storage=storage)
# Создаем планировщик
scheduler = AsyncIOScheduler()

# Подключение к базе данных
connect = sqlite3.connect(f"{database}")
sql = connect.cursor()


