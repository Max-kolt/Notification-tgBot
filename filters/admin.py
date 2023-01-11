from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
import os


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        admin = os.environ.get("ADMIN")
        if admin == message.from_user.id:
            return True
        return False

