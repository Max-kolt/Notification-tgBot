from aiogram import Dispatcher
from utils.weather import get_current_forecast
from db_executor import get_user_info


async def weather_notification(dp: Dispatcher, user_id: int):
    user = get_user_info(user_id)
    forecast = await get_current_forecast(user[1])
    await dp.bot.send_message(user_id, f'~~~Погода на сегодня~~~\n Дата: {forecast["date"]}\n'
                                       f'{str(forecast["temperature_celsius"])[:4]}° ожидается {forecast["icon"]}')
