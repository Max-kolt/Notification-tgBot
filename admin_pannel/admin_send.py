from loader import bot
import os
from aiogram.dispatcher import FSMContext


async def send_admin_feedback(state: FSMContext):
    data = await state.get_data()

    await bot.send_message(os.environ.get("ADMIN"), f'<u><b>Пришел новый отзыв!!!</b></u>\n'
                                      f'Пользователь: {data["username"]}\n'
                                      f'Описание: {data["letter"]}\n'
                                      f'Оценка: {data["grade"]}/5')
