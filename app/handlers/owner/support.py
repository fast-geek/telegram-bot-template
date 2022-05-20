from aiogram import Bot, F
from aiogram.types import ContentType, Message

from app import dp, owner_id
from app.ui.commands import owner_commands


@dp.message(~(F.text.in_(owner_commands)), is_owner=True)
async def question_handler(message: Message, bot: Bot):
    reply_message = message.reply_to_message

    if not reply_message or not reply_message.entities:
        return

    user_id, message_id = reply_message.entities[-1].language.split("-")

    if user_id in (bot.id, owner_id):
        return

    await bot.send_message(
        chat_id=user_id,
        reply_to_message_id=message_id,
        text=f"👨🏻‍💻 <b>Сообщение от администратора:</b>\n\n" f"{message.html_text}",
    )

    await message.answer(
        f"<b>✅ Ответ передан пользователю {message.from_user.full_name}</b>"
    )
