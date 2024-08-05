from aiogram import F, Router
from aiogram.types import CallbackQuery

from handlers.user_private import cmd_start
from markups.markups import markups
from config import language

callback_router = Router()


async def handle_callback(callback: CallbackQuery, text: str, buttons: list) -> None:
    markup = await markups.create_inline(buttons)
    await callback.message.edit_text(text, reply_markup=markup)

@callback_router.callback_query(F.data == 'start')
async def start(callback: CallbackQuery):
    text = language.start_text(callback.from_user.full_name)
    buttons = language.start_buttons
    await handle_callback(callback, text, buttons)

@callback_router.callback_query(F.data == 'cart')
async def call_cart(callback: CallbackQuery) -> None:
    text = language.cart_info_text
    buttons = language.cart_buttons
    await handle_callback(callback, text, buttons)

@callback_router.callback_query(F.data == 'how_to_use')
async def how_to_use(callback: CallbackQuery) -> None:
    text = language.how_to_use
    buttons = language.help_buttons
    await handle_callback(callback, text, buttons)

@callback_router.callback_query(F.data == 'support')
async def call_support(callback: CallbackQuery) -> None:
    text = language.support_info_text
    buttons = language.support_buttons
    await handle_callback(callback, text, buttons)