from aiogram import types, Dispatcher
from dop import dp, bot
from keyboards.client_kb import kb_client
from keyboards.client_kb import lkkb_client
from keyboards.client_kb import obkb_client
from keyboards.client_kb import sskb_client
from keyboards.client_kb import zvkb_client
from keyboards.client_kb import ka_client

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


import sqlite3 as sq

keyboard = 1

def sql_start():
    global base, cur

# приветствие
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, политехник! Команда Объединенного Студенческого Совета нашего\
 университета создала этого бота для помощи решения вопросов, касающихся общежитий и Студенческого Совета!\n\n\
Чтобы начать, нажми кнопку или отправь сообщение!', reply_markup=kb_client)


class Form(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name', state(), чтобы указать, что этот состояние


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # открыть словарь дата
        data['name'] = message.text

    await Form.next()
    await message.reply(f'Вы выбрали общежитие {message.text}')
    user = message.from_user.id
    print(user, message.text)

    # добавление нового или обновление старого
    base = sq.connect('basa.db')
    cur = base.cursor()
    dorm_id = cur.execute(f'select id from main.dorms where dorm == {message.text};').fetchone()
    dorm_id = dorm_id[0]

    isreg = cur.execute(f'select dorm from dorms_of_users where user_id == {user};').fetchone()

    if (isreg == None):
        cur.execute(f'INSERT INTO main.dorms_of_users(user_id, dorm) VALUES ({user}, {dorm_id});')
    else:
        cur.execute(f'UPDATE dorms_of_users SET dorm = {dorm_id} WHERE user_id == {user}')

    base.commit()
    base.close()

async def lk(message: types.Message):
    await bot.send_message(message.from_user.id, 'Личный кабинет', reply_markup=lkkb_client)


async def ob(message: types.Message):
    await bot.send_message(message.from_user.id, 'Общежитие', reply_markup=obkb_client)
    await Form.name.set()


async def ss(message: types.Message):
    await bot.send_message(message.from_user.id, 'Студсовет', reply_markup=sskb_client)


async def zv(message: types.Message):
    await bot.send_message(message.from_user.id, 'Задать вопрос', reply_markup=zvkb_client)

async def zvo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отправьте свой вопрос по адресу: студсовет@mail.ru', reply_markup=zvkb_client)

async def ka(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь вы позже увидите контакты администарции', reply_markup=ka_client)


async def enter_from_bd(message: types.Message):
    for i in cur.execute('SELECT * FROM ega').fetchall():   #  fetchall(), вовзращается в виде кортежа 2 элемента
        await bot.send_message(message.from_user.id, f"dsa {i[0]} {i[1]}")

async def back(message: types.Message):
    await bot.send_message(message.from_user.id, 'Назад', reply_markup=kb_client)


async def plug(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.text}', reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):  # аннотация типов
    dp.register_message_handler(greeting, commands=['start'])
    dp.register_message_handler(lk, Text(equals='Личный кабинет'))
    dp.register_message_handler(ob, Text(equals='Общежития'))
    dp.register_message_handler(ss, Text(equals='Студенческий совет'))
    dp.register_message_handler(zv, Text(equals='Задать вопросы'))
    dp.register_message_handler(ka, Text(equals='Контакты'))
    dp.register_message_handler(enter_from_bd, Text(equals='Регистрация'))
    dp.register_message_handler(back, Text(equals='Отменить действие'))
    dp.register_message_handler(zvo, Text(equals='Отправить'))
    dp.register_message_handler(ka, Text(equals='Дублировать информацию'))
    dp.register_message_handler(back, Text(equals='Назад'))
    #########
    dp.register_message_handler(plug, Text(equals='Информация'))
    dp.register_message_handler(plug, Text(equals='Мероприятия'))
    dp.register_message_handler(plug, Text(equals='Задать вопрос'))
    dp.register_message_handler(plug, Text(equals='Авторизация'))





