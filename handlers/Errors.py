from loader import dp
from filters import IsRegistered, IsNotRegistered
from states import register, add_notes
from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.message_handler(state=[register.time_weather_notify, add_notes.time_notify])
async def time_error(message: types.Message, state: FSMContext):
    await message.answer("Ты допустил ошибку. Попробуй еще раз!\n"
                         "Формат: hh:mm (например, 09:30)")


@dp.message_handler(state=add_notes.date_notify)
async def date_error(message: types.Message, state: FSMContext):
    await message.answer("Ты допустил ошибку. Попробуй еще раз!\n"
                         "Формат: dd-mm-yy (например, 31-12-22)")


@dp.message_handler()
async def unknown_cmd(message: types.Message):
    await message.answer("Не понимаю о чем ты 🙁\n"
                         "Напиши что-нибудь понятное")