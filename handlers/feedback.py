from aiogram.dispatcher import FSMContext

from loader import dp
from filters import IsRegistered
from aiogram import types
from keyboards.default import cancel_menu, main_menu
from states import feedback
from admin_pannel import send_admin_feedback
from db_executor import new_feedback


@dp.message_handler(IsRegistered(), state=feedback.states, text="Отмена❌")
async def cancel_note(message: types.Message, state: FSMContext):  # отмена записи
    await state.reset_data()
    await state.finish()
    await message.answer('Запись прекращена', reply_markup=main_menu)


@dp.message_handler(IsRegistered(), commands=["feedback"])
@dp.message_handler(IsRegistered(), text=["Оставить отзыв✏", "Оставить отзыв", "Отзыв"])
async def feedback_question(message: types.Message):
    await message.answer('Напиши свой отзыв!\nТакже буду очень благодарен если ты поделишься своими идеям'
                         'для улучшения меня 😊 \n А то мой разработчик очень занят, а сам я не знаю чего хочу 😕',
                         reply_markup=cancel_menu)
    await feedback.letter.set()


@dp.message_handler(IsRegistered(), state=feedback.letter)
async def get_letter(message: types.Message, state: FSMContext):
    letter = message.text
    await state.update_data(letter=letter)
    await message.answer('Теперь оцени меня от 1 до 5')
    await feedback.grade.set()


@dp.message_handler(IsRegistered(), lambda message: 1 <= int(message.text) <= 5, state=feedback.grade)
async def get_grade(message: types.Message, state: FSMContext):
    grade = message.text
    await state.update_data(grade=grade, username=message.from_user.username, user_id=message.from_user.id)
    await new_feedback(state)
    await send_admin_feedback(state)
    await state.finish()
    await message.answer('Спасибо за отзыв! Мой разработчик обязательно его прочтет 😋', reply_markup=main_menu)
