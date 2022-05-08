from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='5233751354:AAFsyIPagpgdW7K2z6W_n6V2BviXoesPKsk')
dp = Dispatcher(bot, storage=storage)  # объект для хэндлеров
