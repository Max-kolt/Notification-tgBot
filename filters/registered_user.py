from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from db_executor import select_user


class IsNotRegistered(BoundFilter):
    async def check(self, message: types.Message):
        return not select_user(message.from_user.id)


class IsRegistered(BoundFilter):
    async def check(self, message: types.Message):
        return select_user(message.from_user.id)
