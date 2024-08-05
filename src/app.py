import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import types
import aiogram_dialog

from filters.chat_types import ChatTypeFilter
from callbacks import callback_router
from handlers.user_private import handler_router
from config import language
from loader import dp, bot
import schedules


async def on_startup():
    logging.basicConfig(
        level=logging.INFO, 
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        stream=sys.stdout
        )
    logging.info("Starting bot")
    webhook = await bot.get_webhook_info()
    print("======== SET WEBHOOK ========")
    print(webhook)

    # await create_db()

async def on_shutdown(bot: Bot):
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await bot.session.close()
    webhook = await bot.delete_webhook(drop_pending_updates=True)
    logging.warning("Bot down", webhook)

def add_routes(dp):
    dp.include_router(callback_router)
    dp.include_router(handler_router)

async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    # dp.update.middleware(DataBaseSession(session_pool=session_maker))

    dp.message.filter(ChatTypeFilter(["private"]))
    add_routes(dp)
    
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), on_startup=schedules.on_startup)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")