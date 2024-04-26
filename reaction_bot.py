import asyncio
import time
from aiogram import Bot, Dispatcher, types, F
import logging
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import ReactionTypeEmoji

from config import TOKEN

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum\nXurmatli {message.from_user.mention_html()}</b>")


@dp.message(Command("reaction"))
async def cmd_reaction(message: types.Message):
    reaction_message = await message.answer("Salom")
    time.sleep(5)
    await message.bot.set_message_reaction(
        chat_id=message.chat.id,
        message_id=reaction_message.message_id,
        reaction=[ReactionTypeEmoji(emoji='⚡️')],
        is_big=True
    )


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
