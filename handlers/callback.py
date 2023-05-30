from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько яблок на березе??"
    answer = [
        "1",
        "2",
        "0",
        "400",
        "че",
        "проще общайся",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="книги читай иди",
        open_period=5,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Сколько??"
    answer = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="неуч",
        # open_period=5,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")