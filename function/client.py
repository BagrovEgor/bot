from aiogram import types, Dispatcher
from dop import dp, bot
from keyboards.client_kb import kb_client
from aiogram.dispatcher.filters import Text


# приветствие
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, студенты политеха разработали этого бота для тебя',
                           reply_markup=kb_client)


async def lk(message: types.Message):
    await bot.send_message(message.from_user.id, 'ЛК')


async def ob(message: types.Message):
    await bot.send_message(message.from_user.id, 'Общага')


async def ss(message: types.Message):
    await bot.send_message(message.from_user.id, 'Студ совет')


async def zv(message: types.Message):
    await bot.send_message(message.from_user.id, 'ЗВ')


@dp.message_handler(commands=['Контакты администрации'])
async def ka(message: types.Message):
    await bot.send_message(message.from_user.id, 'КА')

def register_handlers_client(dp: Dispatcher):  # аннотация типов
    dp.register_message_handler(greeting, commands=['start'])
    dp.register_message_handler(lk, Text(equals='Личный кабинет'))
    dp.register_message_handler(ob, Text(equals='Общежития'))
    dp.register_message_handler(ss, Text(equals='Студенческий_совет'))
    dp.register_message_handler(zv, Text(equals='Задать_вопрос'))
    dp.register_message_handler(ka, Text(equals='Контакты'))
