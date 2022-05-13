from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='5241149232:AAEu-7_SdfpJCYuc7935X-6omy0QoE_NBNA')
dp = Dispatcher(bot, storage=storage)  # объект для хэндлеров
