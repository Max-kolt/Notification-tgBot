import sys

from loader import scheduler


async def on_startup(dp):

    import filters
    filters.setup(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    from utils.set_schedulers import set_weather_schedulers, set_note_schedulers
    await set_weather_schedulers(dp)
    await set_note_schedulers(dp)
    scheduler.start()

    print("Бот запущен")


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)