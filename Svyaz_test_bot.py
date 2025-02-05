from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import Bot_config
import Svyaz_test_voprosy

bot = Bot(token =Bot_config.API)
dp = Dispatcher(bot, storage = MemoryStorage())






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)