from loader import dp
from filters import IsRegistered, IsNotRegistered
from states import register, add_notes, feedback
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.default import main_menu


'''
@dp.message_handler(IsRegistered(), state=[feedback.states, add_notes.states], text="Отмена❌")
async def cancel_note(message: types.Message, state: FSMContext):  # отмена записи
    await state.reset_data()
    await state.finish()
    await message.answer('Запись прекращена', reply_markup=main_menu)
'''


@dp.message_handler(state=feedback.grade)
async def grade_feedback_error(message: types.Message):
    await message.answer('Ты допустил ошибку. Попробуй еще раз!\n'
                         'Ты должен ввести цифру от 1 до 5 включая')


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