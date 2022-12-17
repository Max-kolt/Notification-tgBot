import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import API_TOKEN, database

# Создаем бота
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)

# хранилище состояний
storage = MemoryStorage()

# Создаем диспетчер
dp = Dispatcher(bot, storage=storage)


try:
    connect = sqlite3.connect(f"{database}")
    sql = connect.cursor()
except Exception as ex:
    print(ex)
    print("Не получилось подключиться к базе данных")


