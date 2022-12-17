async def on_startup(dp):

    import filters
    filters.setup(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print("Бот запущен")


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
