from loader import dp
from aiogram import types
from filters import IsRegistered
from db_executor import select_user_info


@dp.message_handler(IsRegistered(), commands=['settings'])
@dp.message_handler(IsRegistered(), text=['Настройки⚙', 'Настройки', 'настройки'])
async def give_settings(message: types.Message):
    user = select_user_info(message.from_user.id)
    await message.answer(f'⚙Настройки⚙\nДля того чтобы изменить жми на команду\n\n'
                         f'Имя: {user[0]}\n/change_name\n\n'
                         f'Город: {user[1]}\n /change_city\n\n'
                         f'Оповещение о погоде: {user[2]}\n /change_weatify\n\n'
                         f'Время оповещения о погоде: {user[3]}\n /change_time_wn\n\n'
                         f'Составление аналитики: {user[4]}\n /change_analytics\n\n')

