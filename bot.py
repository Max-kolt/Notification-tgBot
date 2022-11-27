from aiogram import Bot, types, Dispatcher, executor
import logging
from config import API_TOKEN

from Weather_forecast import weather as wf


logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)

dp = Dispatcher(bot)

users_registration = []


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply(f"Hello {message.from_user.first_name}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
