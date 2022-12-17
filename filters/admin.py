from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
from config import admins


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        for admin in admins:
            if admin == message.from_user.id:
                return True
        return False

