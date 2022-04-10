from aiogram import types, Dispatcher
from dop import dp, bot
from keyboards.client_kb import kb_client
from keyboards.client_kb import lkkb_client
from keyboards.client_kb import obkb_client
from keyboards.client_kb import sskb_client
from keyboards.client_kb import zvkb_client

from aiogram.dispatcher.filters import Text

import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('basa.db')
    cur = base.cursor()



# приветствие
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, политехник! Команда Объединенного Студенческого Совета нашего\
 университета создала этого бота для помощи решения вопросов, касающихся общежитий и Студенческого Совета!\n\n\
Чтобы начать, нажми кнопку или отправь сообщение!', reply_markup=kb_client)


async def lk(message: types.Message):
    await bot.send_message(message.from_user.id, 'ЛК', reply_markup=lkkb_client)


async def ob(message: types.Message):
    await bot.send_message(message.from_user.id, 'Общага', reply_markup=obkb_client)


async def ss(message: types.Message):
    await bot.send_message(message.from_user.id, 'Студсовет', reply_markup=sskb_client)


async def zv(message: types.Message):
    await bot.send_message(message.from_user.id, 'ЗВ', reply_markup=zvkb_client)


async def ka(message: types.Message):
    await bot.send_message(message.from_user.id, 'КА')

async def enter_from_bd(message: types.Message):
    for i in cur.execute('SELECT * FROM ega').fetchall():
        await bot.send_message(message.from_user.id, f"dsa {i[0]} {i[1]}")

def register_handlers_client(dp: Dispatcher):  # аннотация типов
    dp.register_message_handler(greeting, commands=['start'])
    dp.register_message_handler(lk, Text(equals='Личный кабинет'))
    dp.register_message_handler(ob, Text(equals='Общежития'))
    dp.register_message_handler(ss, Text(equals='Студенческий совет'))
    dp.register_message_handler(zv, Text(equals='Задать вопросы'))
    dp.register_message_handler(ka, Text(equals='Контакты'))
    dp.register_message_handler(enter_from_bd, Text(equals='Регистрация'))

