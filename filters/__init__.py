from aiogram import Dispatcher
from .registered_user import IsNotRegistered, IsRegistered


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsNotRegistered, IsRegistered)
