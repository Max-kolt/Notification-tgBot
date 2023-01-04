from keyboards.default import main_menu
from loader import dp, scheduler
from filters import IsRegistered
from db_executor import get_user_info
from db_executor import update_city, update_name, \
    update_analytics, update_weather_notify, \
    update_time_weather_notify, verify_time_wn, \
    verify_analytics, verify_weather_notify
from states import register
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from scheduler import weather_notification


@dp.message_handler(IsRegistered(), commands=['settings'])
@dp.message_handler(IsRegistered(), text=['Настройки⚙', 'Настройки', 'настройки'])
async def give_settings(message: types.Message):
    user = get_user_info(message.from_user.id)
    await message.answer(f'⚙Настройки⚙\nДля того чтобы изменить жми на команду\n\n'
                         f'Имя: {user[0]}\n/change_name\n\n'
                         f'Город: {user[1]}\n /change_city\n\n'
                         f'Оповещение о погоде: {user[2]}\n /change_weatify\n\n'
                         f'Время оповещения о погоде: {user[3]}\n /change_time_wn\n\n'
                         f'Составление аналитики: {user[4]}\n /change_analytics\n\n')


# _______________ Change name _______________
@dp.message_handler(IsRegistered(), commands=['change_name'])
async def name_question(message: types.Message):
    await message.answer("Напиши свое новое имя", reply_markup=ReplyKeyboardRemove())
    await register.name.set()


@dp.message_handler(IsRegistered(), state=register.name)
async def change_name(message: types.Message, state: FSMContext):
    update_name(message.from_user.id, message.text)
    await message.answer(f"Имя успешно изменено на <b>{message.text}</b>", reply_markup=main_menu)
    await state.finish()


# _______________ Change city _______________
@dp.message_handler(IsRegistered(), commands=['change_city'])
async def city_question(message: types.Message):
    await message.answer("Напиши новый город", reply_markup=ReplyKeyboardRemove())
    await register.city.set()


@dp.message_handler(IsRegistered(), state=register.city)
async def change_city(message: types.Message, state: FSMContext):
    update_city(message.from_user.id, message.text)
    await message.answer(f"Город успешно изменен на <b>{message.text}</b>", reply_markup=main_menu)
    await state.finish()


# _______________ Change weather notify_______________
@dp.message_handler(IsRegistered(), commands=['change_weatify'])
async def change_weather_notify(message: types.Message):
    user_id = message.from_user.id
    if verify_weather_notify(user_id):
        update_weather_notify(user_id, False)
        await message.answer(f"Оповещение о прогнозе погоды <b>отключено</b>")
    else:
        update_weather_notify(user_id, True)
        await message.answer(f"Оповещение о прогнозе погоды <b>включено</b>")
        if verify_time_wn(user_id):
            await message.answer(f"Оповещение о прогнозе погоды <b>включено</b>\n"
                                 f'В какое время тебя оповещать?', reply_markup=ReplyKeyboardRemove())
            await register.time_weather_notify.set()
        else:
            user_info = get_user_info(user_id)
            time = user_info[3]
            scheduler.add_job(weather_notification,
                              hour=time[:2],
                              minute=time[3:],
                              args=(dp, user_id),
                              id=str(user_id))


# _______________ Change time weather notify_______________
@dp.message_handler(IsRegistered(), commands=['change_time_wn'])
async def time_weather_notify_question(message: types.Message):
    await message.answer("Введи новое время", reply_markup=ReplyKeyboardRemove())
    await register.time_weather_notify.set()


@dp.message_handler(IsRegistered(), state=register.time_weather_notify, regexp=r"(?<!\d)(?:[0-1][0-9]|2[0-3]):(?:[0-5]["
                                                                               r"0-9])(?!\d)")
async def change_time_weather_notify(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    time = message.text
    update_time_weather_notify(message.from_user.id, time)
    await message.answer(f"Время успешно изменено на <b>{message.text}</b>", reply_markup=main_menu)
    if scheduler.get_job(job_id=str(user_id)) is None:
        scheduler.add_job(weather_notification,
                          trigger='cron',
                          hour=int(time[:2]),
                          minute=int(time[3:]),
                          args=(dp, user_id),
                          id=str(user_id))
    else:
        scheduler.remove_job(str(user_id))
        scheduler.add_job(weather_notification,
                          trigger='cron',
                          hour=int(time[:2]),
                          minute=int(time[3:]),
                          args=(dp, user_id),
                          id=str(user_id))

    await state.finish()


# _______________ Change analytics_______________
@dp.message_handler(IsRegistered(), commands=['change_analytics'])
async def analytics_question(message: types.Message):
    user_id = message.from_user.id
    if verify_analytics(user_id):
        update_analytics(user_id, False)
        await message.answer("Аналитика <b>отключена</b>")
    else:
        update_analytics(user_id, True)
        await message.answer("Аналитика <b>включена</b>")
