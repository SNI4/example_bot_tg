from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

bot = bot(config.TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemortStorage()
dp = Dispatcher(bot, storage=storage)