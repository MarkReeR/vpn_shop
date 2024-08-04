from aiogram import F, Router
from aiogram.types import CallbackQuery

from markups import markups
from localization import ru as language

callback_router = Router()


@callback_router.callback_query(F.data == 'cart')
async def call_cart(callback: CallbackQuery) -> None:
    await callback.answer("")
    await callback.message.edit_text("В разработек")

@callback_router.callback_query(F.data == 'help')
async def call_help(callback: CallbackQuery) -> None:
    await callback.answer("")
    await callback.message.edit_text(language.help_data, 
                                     reply_markup=await markups.create_inline([[language.cart, 'cart'], [language.help, 'help'], [language.support, 'support']]))

@callback_router.callback_query(F.data == 'support')
async def call_support(callback: CallbackQuery) -> None:
    await callback.answer("")
    await callback.message.edit_text("В разработек\nhttps://youtu.be/dQw4w9WgXcQ?si=Ug5KS8ekxJiV3-le")

# TODO Go back