from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from filters import IsNotRegistered
from keyboards.default import yes_no_menu, main_menu
from keyboards.inline import ikb_yes_no
from loader import dp
from states import register
from db_executor import add_new_user


@dp.message_handler(IsNotRegistered(), text="Давай!")
async def whats_your_name(message: types.Message):
    await message.answer("Отлично! Тогда ответь пожалуйста на несколько вопросов. 😊\n\n"
                         "🌒(1/4)Как тебя зовут?", reply_markup=ReplyKeyboardRemove())
    await register.name.set()


@dp.message_handler(IsNotRegistered(), state=register.name)
async def whats_your_city(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(f"🌓(2/4){name}, в каком городе проживаешь?🏙\n\n"
                         f"Пиши полное название, для корректной работы 🤓")
    await register.city.set()


@dp.message_handler(IsNotRegistered(), state=register.city)
async def weather_notify(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    await message.answer("Отлично! Мы на верном пути)\n"
                         "🌔(3/4) Тебя оповещать о погоде?🌧",
                         reply_markup=ikb_yes_no)
    await register.weather_notify.set()


@dp.callback_query_handler(IsNotRegistered(), text='Yes', state=register.weather_notify)
async def time_weather_notify(call: CallbackQuery, state: FSMContext):
    await state.update_data(weather_notify=True)
    await call.message.edit_text("🌔(3,5/4)В какое время тебя оповещать?🌤\n\n"
                                 "🕓 Пиши в формате: hh:mm\n"
                                 "Рекомендую утром, когда ты наслаждаешься завтраком😉")
    await register.time_weather_notify.set()


@dp.callback_query_handler(IsNotRegistered(), text='No', state=register.weather_notify)
async def analitycs(call: CallbackQuery, state: FSMContext):
    await state.update_data(weather_notify=False, time_weather_notify=None)
    await call.message.delete()
    await call.message.answer("Эх, а я так хотел тебе писать по утрам.🙁\n"
                              "Последний вопрос!\n\n"
                              "🌕(4/4) Делать ли для тебя аналитику твоих записей?",
                              reply_markup=yes_no_menu)
    await register.analytics.set()


@dp.message_handler(IsNotRegistered(), state=register.time_weather_notify, regexp=r"\d\d[-:]\d\d")
async def analitycs(message: types.Message, state: FSMContext):
    time = message.text
    await state.update_data(time_weather_notify=time)
    await message.answer("Вот и он, последний вопрос!\n"
                         "🌕(4/4) Делать ли для тебя аналитику твоих записей?",
                         reply_markup=yes_no_menu)
    await register.analytics.set()


@dp.message_handler(IsNotRegistered(), state=register.time_weather_notify)
async def analitycs(message: types.Message, state: FSMContext):
    await message.answer("Ты допустил ошибку. Попробуй еще раз!\n"
                         "Формат: hh:mm (например, 09:30)")
    await register.time_weather_notify.set()


@dp.message_handler(IsNotRegistered(), state=register.analytics, text=["Да", "Нет"])
async def register_new_user(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.lower() == "да":
        await state.update_data(analytics=True)
    else:
        await state.update_data(analytics=False)

    data = await state.get_data()
    add_new_user(_id=message.from_user.id,
                 name=data.get('name'),
                 city=data.get('city'),
                 weather_notify=data.get('weather_notify'),
                 time_weather_notify=data.get('time_weather_notify'),
                 analytics=data.get('analytics'))

    await message.answer(f"Спасибо, {data.get('name')}!\n"
                         f"Ты у нас живешь в {data.get('city')}.\n"
                         f"Оповещение о погоде: {data.get('weather_notify')} (время: {data.get('time_weather_notify')})\n"
                         f"Составление аналитики: {data.get('analytics')}"
                         f"\n\n"
                         f"Теперь я полностью готов к работе😼",
                         reply_markup=main_menu)
    await state.finish()


