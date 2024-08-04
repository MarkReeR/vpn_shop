import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import types

# from aiogram.types import ReplyKeyboardMarkup

import config
from loader import dp, bot
from markups import markups
from callbacks import callback_router
from localization import ru as language



@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    # TODO
    # if await user.is_admin:
    #     markup.add(types.KeyboardButton(constants.language.admin_panel))

    await message.answer_sticker('CAACAgIAAxkBAAM6Zq55RNyW6hyhfjZHHV49y6kl-nYAAhsAAwnHpAij-M9iBHukZjUE')
    # TODO add {cart} ...
    values = [[language.cart, 'cart'], [language.help, 'help'], [language.support, 'support']]
    markup = await markups.create_inline(values)
    await message.answer(f"Приветствую, {html.bold(message.from_user.full_name)}!\n"
                        "Ты можешь использовать:\n"
                        f"  1) /{values[0][1]} чтобы ознакомится с наим товаром.\n"
                        f"  2) /{values[1][1]} для того чтобы узнать установить VPN\n"
                        f"  3) /{values[2][1]} чтобы связатся с нами.", 
                        reply_markup=markup)

@dp.message()
async def answer(message: Message) -> None:
    # If the user writes something other than commands
    try:
        await message.reply("Используйте команды.")
    except TypeError:
        await message.answer("Nice try!")

async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")

async def main() -> None:
        dp.include_router(callback_router)
        await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        on_shutdown()