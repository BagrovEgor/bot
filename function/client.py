from aiogram import types, Dispatcher
from dop import dp, bot
from keyboards.client_kb import kb_client
# from keyboards.client_kb import lkkb_client
from keyboards.client_kb import obkb_client
from keyboards.client_kb import sskb_client
from keyboards.client_kb import zvkb_client
from keyboards.client_kb import usekb_client
from keyboards.client_kb import liverskb_client
from keyboards.client_kb import entrantskb_client
from keyboards.client_kb import benefiterskb_client

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import sqlite3 as sq


# приветствие
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, политехник! Команда Объединенного Студенческого Совета нашего\
 университета создала этого бота для помощи решения вопросов, касающихся общежитий и Студенческого Совета!\n\n\
Чтобы начать, нажми кнопку или отправь сообщение!', reply_markup=kb_client)

7
class Form(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name', state(), чтобы указать, что этот состояние


class AnsForm(StatesGroup):
    name = State()


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    base = sq.connect('basa.db')
    cur = base.cursor()

    async with state.proxy() as data:  # открыть словарь дата
        if message.text != 'Назад':
            data['name'] = cur.execute(f"select id from main.dorms where dorm == '{message.text}';").fetchone()
            dorm_num = data['name']
            dorm_num = dorm_num[0]

    await Form.next()
    if message.text != 'Назад':
        i = cur.execute('SELECT * FROM info_dorms').fetchall()
        # print(dorm_num)
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
                                   f"Общежитие №{message.text}\n\n"
                                   f"Адрес: {i[dorm_num - 1][1]}\n\n"
                                   f"Заведующая: {i[dorm_num - 1][2]}\n\n"
                                   f"Почта: {i[dorm_num - 1][4]}\n\n"
                                   f"Группа ВК: {i[dorm_num - 1][5]}\n\n",
                                   reply_markup=obkb_client)
        await bot.send_location(message.from_user.id, i[dorm_num - 1][6], i[dorm_num - 1][7])
        # await bot.send_message(message.from_user.id, f"*yyy*",
        # reply_markup=obkb_client, parse_mode="Markdown")
        await Form.name.set()

    else:
        await message.reply('Действие выполнено', reply_markup=kb_client)

    base.commit()
    base.close()


'''
async def lk(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Личный кабинет', reply_markup=lkkb_client)
'''


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
    await bot.send_message(message.from_user.id,
                           f'Информация об Администрации СТГ:\n{i[0][0]} \n\n{i[0][1]} \n{i[0][2]}',
                           reply_markup=usekb_client)


async def center_settlement(message: types.Message):
    base = sq.connect('basa.db')
    cur = base.cursor()

    i = cur.execute('SELECT * FROM contact_inf').fetchall()
    base.commit()
    base.close()
    await bot.send_message(message.from_user.id, f'Информация о центре поселения:\n{i[1][0]} \n\n{i[1][1]} \n{i[1][2]}',
                           reply_markup=usekb_client)


async def passport(message: types.Message):
    base = sq.connect('basa.db')
    cur = base.cursor()

    i = cur.execute('SELECT * FROM contact_inf').fetchall()
    base.commit()
    base.close()
    await bot.send_message(message.from_user.id, f'Информация о паспортном столе:\n{i[2][0]} \n{i[3][0]} \n{i[2][2]}',
                           reply_markup=usekb_client)


async def back(message: types.Message):
    await message.reply('Действие выполнено', reply_markup=kb_client)


async def plug(message: types.Message):
    await bot.send_message(message.from_user.id, 'https://vk.com/studg', reply_markup=sskb_client)


async def info_SC(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'ОСС – это орган студенческого самоуправления в Студенческом городке СПбПУ. '
                           'Мы защищаем права и интересы студентов перед администрацией. Наша основная задача - '
                           'улучшение качества жизни в Студгородке. '
                           'Также мы занимаемся организацией мероприятий в общежитиях и университете.\n\n'
                           'Председатель: Перец Алина', reply_markup=sskb_client)


@dp.message_handler(state=AnsForm.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # открыть словарь дата
        data['name'] = message.text

    await AnsForm.next()
    if (message.text != 'Назад' and message.text != 'Нет ответа?'):
        base = sq.connect('basa.db')
        cur = base.cursor()

        answer = cur.execute(f"select Answer from main.FAQ where Question == '{message.text}';").fetchone()
        answer = answer[0]
        await bot.send_message(message.from_user.id, f"{answer}")

        base.commit()
        base.close()
        await AnsForm.name.set()

    elif message.text == 'Назад':
        await message.reply('Действие выполнено', reply_markup=zvkb_client)
    else:
        await bot.send_message(message.from_user.id, 'Обратиться к Администрации СТГ: '
                                                     'Обратиться в Студенческий совет: https://vk.com/studg',
                               reply_markup=zvkb_client)



async def livers(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Проживающим', reply_markup=liverskb_client)
    await AnsForm.name.set()


async def entrants(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Абитуриентам', reply_markup=entrantskb_client)
    await AnsForm.name.set()


async def benefiters(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали раздел: Льготным категориям', reply_markup=benefiterskb_client)
    await AnsForm.name.set()



'''
async def auth(message: types.Message):
    await message.reply('В разработке...', reply_markup=kb_client)
'''


def register_handlers_client(disp: Dispatcher):  # аннотация типов
    # Главное меню
    disp.register_message_handler(greeting, commands=['start'])
    # dp.register_message_handler(lk, Text(equals='Личный кабинет'))
    disp.register_message_handler(ob, Text(equals='Общежития'))
    disp.register_message_handler(ss, Text(equals='Студенческий совет'))
    disp.register_message_handler(zv, Text(equals='Задать вопрос'))
    disp.register_message_handler(useful, Text(equals='Полезное'))

    disp.register_message_handler(useful, Text(equals='Полезное'))
    disp.register_message_handler(back, Text(equals='Назад'))
    # СС
    disp.register_message_handler(info_SC, Text(equals='Кто мы?'))
    disp.register_message_handler(plug, Text(equals='Группа ВК'))

    # ЗВ
    disp.register_message_handler(livers, Text(equals='Проживающим'))
    disp.register_message_handler(entrants, Text(equals='Абитуриентам'))
    disp.register_message_handler(benefiters, Text(equals='Льготным категориям'))


    # Полезное
    disp.register_message_handler(adm_sc, Text(equals='Администрация СТГ'))
    disp.register_message_handler(center_settlement, Text(equals='Центр поселения'))
    disp.register_message_handler(passport, Text(equals='Паспортный стол'))

    # dp.register_message_handler(auth, Text(equals='Авторизация'))
