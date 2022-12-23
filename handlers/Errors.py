from loader import dp
from filters import IsRegistered, IsNotRegistered
from states import register
from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.message_handler(state=register.time_weather_notify)
async def time_weather_again(message: types.Message, state: FSMContext):
    await message.answer("Ты допустил ошибку. Попробуй еще раз!\n"
                         "Формат: hh:mm (например, 09:30)")


