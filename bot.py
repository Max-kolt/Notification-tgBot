from db_executor import get_all_weather_notify_users, get_user_info
from handlers.apsched import weather_notification
from loader import scheduler


async def on_startup(dp):

    import filters
    filters.setup(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    from utils.set_schedulers import set_users_schedulers
    await set_users_schedulers(dp)
    scheduler.start()

    print("Бот запущен")


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
