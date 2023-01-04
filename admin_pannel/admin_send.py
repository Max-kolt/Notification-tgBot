from loader import bot
from config import admins
from aiogram.dispatcher import FSMContext


async def send_admin_feedback(state: FSMContext):
    data = await state.get_data()

    for admin in admins:
        await bot.send_message(admin, f'<u><b>Пришел новый отзыв!!!</b></u>\n'
                                      f'Пользователь: {data["username"]}\n'
                                      f'Описание: {data["letter"]}\n'
                                      f'Оценка: {data["grade"]}/5')
