from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запуск бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('settings', 'Настройки'),
        types.BotCommand('feedback', 'Отзыв'),
        types.BotCommand('change_name', 'Изменить имя'),
        types.BotCommand('change_city', 'Изменить город'),
        types.BotCommand('change_weatify', 'Изменить оповещение о погоде'),
        types.BotCommand('change_time_wn', 'Изменить время оповещения о погоде'),
        types.BotCommand('change_analytics', 'Изменить аналитику'),
        types.BotCommand('create_note', 'Создать запись'),
    ])