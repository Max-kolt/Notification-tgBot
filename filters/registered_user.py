from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from db_executor import verify_user


class IsNotRegistered(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return not verify_user(message.from_user.id)


class IsRegistered(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return verify_user(message.from_user.id)
