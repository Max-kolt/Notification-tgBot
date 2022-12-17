from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    name = State()
    city = State()
    weather_notify = State()
    time_weather_notify = State()
    analytics = State()

