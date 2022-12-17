from aiogram import Dispatcher
from .registered_user import IsNotRegistered, IsRegistered
from .admin import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsNotRegistered)
    dp.filters_factory.bind(IsRegistered)
    dp.filters_factory.bind(IsAdmin)
