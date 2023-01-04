from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    name = State()
    city = State()
    weather_notify = State()
    time_weather_notify = State()
    analytics = State()


class add_notes(StatesGroup):
    description = State()
    date_notify = State()
    time_notify = State()


class feedback(StatesGroup):
    letter = State()
    grade = State()


'''
class note_notify(StatesGroup):
    performed = State()
'''