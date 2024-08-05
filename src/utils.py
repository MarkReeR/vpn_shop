from aiogram import types
import config
from markups.markups import markups

async def sendNoPermission(message: types.Message) -> None:
    await message.answer(
        text=config.language.no_permission,
    )

async def sendStateNotFound(message: types.Message) -> None:
    await message.answer(
        text=config.language.unknown_call_stop_state,
        reply_markup=markups.create([(config.language.back, f"{config.JSON_ADMIN}cancel")])
    )
