from aiogram import types, Dispatcher
from dop import dp, bot
from keyboards.client_kb import kb_client
from keyboards.client_kb import lkkb_client
from keyboards.client_kb import obkb_client
from keyboards.client_kb import sskb_client
from keyboards.client_kb import zvkb_client
from keyboards.client_kb import usekb_client

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import tracemalloc
import sqlite3 as sq

# приветствие
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, политехник! Команда Объединенного Студенческого Совета нашего\
 университета создала этого бота для помощи решения вопросов, касающихся общежитий и Студенческого Совета!\n\n\
Чтобы начать, нажми кнопку или отправь сообщение!', reply_markup=kb_client)


class Form(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name', state(), чтобы указать, что этот состояние


dorm_names = ['0', '1', '3', '4', '4а', '5', '6', '7', '8', '10', '11', '12', '13', '14a', '14б', '14ц', '15',
              '16', '17', '18', '18', '19', '20']


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    print('ok')
    async with state.proxy() as data:  # открыть словарь дата
        if message.text != 'Назад':
            data['name'] = dorm_names.index(message.text)
            dorm_num = data['name']

    await Form.next()
    if message.text != 'Назад':
        base = sq.connect('basa.db')
        cur = base.cursor()
        user = message.from_user.id
        print(user)
        '''
        dorm_id = cur.execute(f'select dorm from main.dorms_of_users where user_id == {user};').fetchone()
        dorm_id = dorm_id[0]
        '''
        i = cur.execute('SELECT * FROM info_dorms').fetchall()

        if dorm_num == 3:
            await bot.send_message(message.from_user.id,
                                   f'Общежитие №{message.text}\n\n'
                                   f'Адрес: {i[dorm_num - 1][1]}\n\n'
                                   f'Заведующая: {i[dorm_num - 1][2]}\n\n'
                                   f'Администратор: {i[dorm_num - 1][3]}\n\n'
                                   f'Почта: {i[dorm_num - 1][4]}\n\n'
                                   f'Группа ВК: {i[dorm_num - 1][5]}\n\n',
                                   reply_markup=obkb_client)
        else:
            await bot.send_message(message.from_user.id,
                                   f"Общежитие №{message.text}*\n\n"
                                   f"Адрес: {i[dorm_num - 1][1]}\n\n"
                                   f"Заведующая: {i[dorm_num - 1][2]}\n\n"
                                   f"Почта: {i[dorm_num - 1][4]}\n\n"
                                   f"Группа ВК: {i[dorm_num - 1][5]}\n\n",
                                   reply_markup=obkb_client)
        await bot.send_location(message.from_user.id, i[dorm_num - 1][6], i[dorm_num - 1][7])
        # await bot.send_message(message.from_user.id, f"*yyy*",
                                   # reply_markup=obkb_client, parse_mode="Markdown")

        '''
        # добавление нового или обновление старого
        dorm_id = cur.execute(f'select id from main.dorms where dorm == {dorm_num};').fetchone()
        dorm_id = dorm_id[0]

        isreg = cur.execute(f'select dorm from dorms_of_users where user_id == {user};').fetchone()

        if (isreg == None):
            cur.execute(f'INSERT INTO main.dorms_of_users(user_id, dorm) VALUES ({user}, {dorm_id});')
        else:
            cur.execute(f'UPDATE dorms_of_users SET dorm = {dorm_id} WHERE user_id = {user};')
        '''

        base.commit()
        base.close()

        await Form.name.set()

    else:
        await message.reply('Дейтсвие выполнено', reply_markup=kb_client)




async def lk(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Личный кабинет', reply_markup=lkkb_client)


async def ob(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Общежития', reply_markup=obkb_client)
    await Form.name.set()


async def ss(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Студсовет', reply_markup=sskb_client)


async def zv(message: types.Message):
    await bot.send_message(message.from_user.id, 'В этом разделе вы сможете найти ответы на все частые вопросы, '
                                                 'которые появляются у студентов и абитуриентов нашего университета'
                                                 ' в отношении общежитий.', reply_markup=zvkb_client)


async def useful(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Полезное', reply_markup=usekb_client)


async def adm_sc(message: types.Message):
    base = sq.connect('basa.db')
    cur = base.cursor()

    i = cur.execute('SELECT * FROM contact_inf').fetchall()
    base.commit()
    base.close()
    await bot.send_message(message.from_user.id, f'Информация об Администрации СТГ:\n{i[0][0]} \n\n{i[0][1]} \n{i[0][2]}', reply_markup=usekb_client)


async def сenter_settlement(message: types.Message):
    base = sq.connect('basa.db')
    cur = base.cursor()

    i = cur.execute('SELECT * FROM contact_inf').fetchall()
    base.commit()
    base.close()
    await bot.send_message(message.from_user.id, f'Информация о центре поселения:\n{i[1][0]} \n\n{i[1][1]} \n{i[1][2]}', reply_markup=usekb_client)


async def passport(message: types.Message):
    base = sq.connect('basa.db')
    cur = base.cursor()

    i = cur.execute('SELECT * FROM contact_inf').fetchall()
    base.commit()
    base.close()
    await bot.send_message(message.from_user.id, f'Информация о паспортном столе:\n{i[2][0]} \n\n{i[2][2]}', reply_markup=usekb_client)


async def back(message: types.Message):
    await message.reply('Действие выполнено', reply_markup=kb_client)


async def plug(message: types.Message):
    await bot.send_message(message.from_user.id, 'https://vk.com/studg', reply_markup=sskb_client)

async def info_SC(message: types.Message):
    await bot.send_message(message.from_user.id, 'ОСС – это орган студенческого самоуправления в Студенческом городке СПбПУ. '
                                                 'Мы защищаем права и интересы студентов перед администрацией. Наша основная задача - улучшение качества жизни в Студгородке. '
                                                 'Также мы занимаемся организацией мероприятий в общежитиях и университете.\n\n'
                                                 'Председатель: Перец Алина', reply_markup=sskb_client)

async def applicants(message: types.Message):
    await message.reply('Абитуриентам', reply_markup=zvkb_client)


async def students(message: types.Message):
    await message.reply('Студентам', reply_markup=zvkb_client)


async def NoQ(message: types.Message):
    await bot.send_message(message.from_user.id,'Обратиться к Администрации СТГ: '
                                                'Обратиться в Студенческий совет: https://vk.com/studg', reply_markup=zvkb_client)



def register_handlers_client(dp: Dispatcher):  # аннотация типов
    ## Главное меню
    dp.register_message_handler(greeting, commands=['start'])
    dp.register_message_handler(lk, Text(equals='Личный кабинет'))
    dp.register_message_handler(ob, Text(equals='Общежития'))
    dp.register_message_handler(ss, Text(equals='Студенческий совет'))
    dp.register_message_handler(zv, Text(equals='Задать вопрос'))
    dp.register_message_handler(useful, Text(equals='Полезное'))

    dp.register_message_handler(useful, Text(equals='Полезное'))
    dp.register_message_handler(back, Text(equals='Назад'))
    ######### СС
    dp.register_message_handler(info_SC, Text(equals='Кто мы?'))
    dp.register_message_handler(plug, Text(equals='Группа ВК'))

    #ЗВ
    dp.register_message_handler(applicants, Text(equals='Абитуриентам'))
    dp.register_message_handler(students, Text(equals='Студентам'))
    dp.register_message_handler(NoQ, Text(equals='Нет ответа?'))
    ## Полезное
    dp.register_message_handler(adm_sc, Text(equals='Администрация СТГ'))
    dp.register_message_handler(сenter_settlement, Text(equals='Центр поселения'))
    dp.register_message_handler(passport, Text(equals='Паспортный стол'))



