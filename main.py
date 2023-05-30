import os
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin, FSM_Admin_mentors, sheduler
import logging
from database.bot_db import sql_create
async def on_startup(_):
    sql_create()
    await sheduler.set_scheduler()

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
FSM_Admin_mentors.register_handlers_fsm_anketa(dp)

admin.register_handlers_admin(dp)

extra.register_handlers_extra(dp)
API_TOKEN = "6272446995:AAHq0rw0lskYkwLOC-_CBJFI0FlBHkt6Wa8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
dp.middleware.setup(LoggingMiddleware())

quiz_questions = {
    "Столица Франции?": "Париж",
    "Какая планета ближе всего к Солнцу?": "Меркурий"
}

user_current_question = {}

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Я - викторина бот. Напиши /quiz, чтобы начать викторину.")

@dp.message_handler(commands=["quiz"])
async def quiz_command(message: types.Message):
    question = random.choice(list(quiz_questions.keys()))
    user_current_question[message.from_user.id] = question
    await message.reply(f"Вопрос: {question}")

@dp.message_handler(commands=["mem"])
async def mem_command(message: types.Message):
    mem_url = "https://vk.com/photo-140602551_457255341?access_key=24e53e911cf2ab05f7"
    await bot.send_photo(chat_id=message.chat.id, photo=mem_url)

@dp.message_handler()
async def text_messages_handler(message: types.Message):
    user_id = message.from_user.id

    if user_id in user_current_question:
        question = user_current_question[user_id]
        if message.text.lower() == quiz_questions[question].lower():
            await message.reply("Правильно!")
        else:
            await message.reply("Неправильно. Попробуй еще раз.")
        del user_current_question[user_id]
    elif message.text.isdigit():
        squared = int(message.text) ** 2
        await message.reply(f"{message.text} в квадрате равно {squared}")
    else:
        await message.reply(message.text)

extra.register_handlers_extra(dp)


if __name__ == "__main__":
    from aiogram import executor
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
