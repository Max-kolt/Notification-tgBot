from aiogram import Dispatcher
from builtin_modules.weather import get_current_forecast
from db_executor import get_user_info, update_note_perform


async def weather_notification(dp: Dispatcher, user_id: int):  # метод планировщика погоды
    user = get_user_info(user_id)
    forecast = await get_current_forecast(user[1])
    await dp.bot.send_message(user_id, f'~~~~~~~~Погода на сегодня~~~~~~~~\n Дата: {forecast["date"]}\n'
                                       f' Город: {user[1]}\n'
                                       f'<b>{str(forecast["temperature_celsius"])[:5]}°</b> ожидается {forecast["icon"]}')


async def note_notification(dp: Dispatcher, user_id: int, note: tuple):  # метод планировщика записей
    await dp.bot.send_message(user_id, f'________Запись________\n\n<b>{note[1]}</b>\n\n '
                                       f'<i>Запись была создана: {note[2]}</i>')
    update_note_perform(note[0])


