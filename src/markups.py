from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from localization import ru as language


class Markups:
    async def create_inline(self, values: list[tuple[str, str] | tuple[tuple[str, str]]]) -> InlineKeyboardMarkup:
        markup = InlineKeyboardBuilder()
        for item in values:
            if isinstance(item[0], tuple):
                markup.add(*[InlineKeyboardButton(text=subitem[0], callback_data=subitem[1]) for subitem in item])
                continue
            markup.add(InlineKeyboardButton(text=item[0], callback_data=item[1]))
        return markup.as_markup()
    
markups = Markups()