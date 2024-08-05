from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import traceback

from markups.markups import markups
from utils import sendStateNotFound
from config import language

handler_router = Router()

@handler_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer_sticker('CAACAgIAAxkBAAM6Zq55RNyW6hyhfjZHHV49y6kl-nYAAhsAAwnHpAij-M9iBHukZjUE')
    text = language.start_text(html.bold(message.from_user.full_name))
    markup = await markups.create_inline(language.start_buttons)
    await message.answer(text, reply_markup=markup)
    
@handler_router.message(Command("cart"))
async def cart_menu(message: Message) -> None:
    text = language.cart_info_text
    markup = await markups.create_inline(language.cart_buttons)
    await message.answer(text,reply_markup=markup)
    
@handler_router.message(Command("how_to_use"))
async def how_to_use(message: Message) -> None:
    text = language.how_to_use
    markup = await markups.create_inline(language.help_buttons)
    await message.answer(text,reply_markup=markup)
    
@handler_router.message(Command("support"))
async def support_menu(message: Message) -> None:
    text = language.support_info_text
    markup = await markups.create_inline(language.support_buttons)
    await message.answer(text,reply_markup=markup)

# @handler_router.message(state="*", content_types=ContentTypes.ANY)
# async def process_message_state(message: Message, state: FSMContext) -> None:
#     state_path = f"callbacks.states.{(await state.get_state()).replace(':', '_')}"

#     try:
#         await importlib.import_module(state_path).execute(callback_query=None, user=users.User(message.chat.id), data=None, message=message, state=state)
#     except ModuleNotFoundError:
#         await sendStateNotFound(message)
#     except:
#         traceback.print_exc()
    
@handler_router.message()
async def answer_if_not_command(message: Message) -> None:
    # If the user writes something other than commands
    try:
        await message.reply(language.unknown_command)
    except TypeError:
        await message.answer(language.nice_try)