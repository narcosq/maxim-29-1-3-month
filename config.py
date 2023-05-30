from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "6272446995:AAHq0rw0lskYkwLOC-_CBJFI0FlBHkt6Wa8"

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = (1803684548, )