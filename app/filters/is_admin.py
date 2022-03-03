from aiogram import types
from aiogram.dispatcher.filters import BaseFilter

from app import admin_ids


class IsAdmin(BaseFilter):
    is_admin: bool

    async def __call__(self, message: types.Message) -> bool:
        return self.is_admin is (message.from_user.id in admin_ids)
