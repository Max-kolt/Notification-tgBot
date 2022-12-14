from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запуск бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('settings', 'Настройки'),
        types.BotCommand('create_note', 'Создать запись'),
        types.BotCommand('feedback', 'Отавить отзыв'),
        types.BotCommand('donate', 'Поддержать разработчика'),
        types.BotCommand('change_name', 'Изменить имя'),
        types.BotCommand('change_city', 'Изменить город'),
        types.BotCommand('change_weatify', 'Изменить оповещение о погоде'),
        types.BotCommand('change_time_wn', 'Изменить время оповещения о погоде'),
        types.BotCommand('change_analytics', 'Изменить аналитику')
    ])
