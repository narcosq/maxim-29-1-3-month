from aiogram import types, Dispatcher


async def delete_sticker(message: types.Message):
    await message.delete()


# @dp.message_handler()
async def bad_words_filter(message: types.Message):
    bad_words = ['мал', 'кот', 'ауе', 'жинди', 'дурак']
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.answer(f"тише брат {message.from_user.full_name}, "
                                 f"сам ты {word}")
            await message.delete()
            # await bot.delete_message(message.chat.id, message.message_id)
            break

    if message.text.startswith('.'):
        # await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()

    if message.text == "dice":
        a = await message.answer_dice()
        # await bot.send_dice(message.chat.id, emoji="⚽️")
        # print(a.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter, content_types=['text'])
    dp.register_message_handler(delete_sticker, content_types=['sticker', 'photo',
                                                               'animation'])