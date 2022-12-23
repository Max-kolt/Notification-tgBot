from aiogram import Dispatcher
from utils.weather import get_current_forecast
from db_executor import get_user_info, update_note_perform
from keyboards.inline import ikb_note_yes_no
from states import note_notify


async def weather_notification(dp: Dispatcher, user_id: int):
    user = get_user_info(user_id)
    forecast = await get_current_forecast(user[1])
    await dp.bot.send_message(user_id, f'~~~~~~~~<b>Погода на сегодня</b>~~~~~~~~\n Дата: {forecast["date"]}\n'
                                       f'{str(forecast["temperature_celsius"])[:4]}° ожидается {forecast["icon"]}')


async def note_notification(dp: Dispatcher, user_id: int, note: tuple):
    await dp.bot.send_message(user_id, f'________<b>Запись</b>________\n\n{note[1]}\n\n Создана: {note[2]}')
    update_note_perform(note[0])


