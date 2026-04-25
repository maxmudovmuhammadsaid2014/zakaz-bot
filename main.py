import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# 👥 user guruhga qo‘shilganda
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    for user in message.new_chat_members:

        text = (
            "👥 Yangi a'zo qo‘shildi!\n\n"
            f"👤 Ism: {user.full_name}\n"
            f"🆔 ID: {user.id}"
        )

        await bot.send_message(CHANNEL_ID, text)
        await message.answer(f"👋 Xush kelibsiz {user.full_name}!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
