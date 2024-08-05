from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Markups:
    async def create_inline(self, values: list[tuple[str, str] | tuple[tuple[str, str]]], sizes: tuple[int] = (2,)) -> InlineKeyboardMarkup:
        markup = InlineKeyboardBuilder()
        if isinstance(values, dict):
            for callback_data, text in values.items():
                markup.add(InlineKeyboardButton(text=text, callback_data=callback_data))
        else:
            for item in values:
                
                if isinstance(item[0], tuple):
                    buttons = [InlineKeyboardButton(text=subitem[0], callback_data=subitem[1]) for subitem in item]
                    markup.add(*buttons)
                else:
                    markup.add(InlineKeyboardButton(text=item[0], callback_data=item[1]))
        return markup.adjust(*sizes).as_markup()
    
markups = Markups()