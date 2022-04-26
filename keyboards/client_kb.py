from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import sqlite3 as sq
from aiogram.dispatcher.filters import Text



kb_back = KeyboardButton('Назад')

# команды
kb1 = KeyboardButton('Личный кабинет')
kb2 = KeyboardButton('Общежития')
kb3 = KeyboardButton('Студенческий совет')
kb4 = KeyboardButton('Задать вопросы')
kb5 = KeyboardButton('Контакты')
kb6 = KeyboardButton('Отменить действие')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # замещает клавиатуру
kb_client.add(kb1).add(kb2).insert(kb3).add(kb4).insert(kb5).add(kb_back)

# Личный кабинет
lkkb1 = KeyboardButton(text='Авторизация')

lkkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
lkkb_client.add(lkkb1).add(kb_back)

# Студенческий совет
sskb1 = KeyboardButton(text='Информация')
sskb2 = KeyboardButton(text='Мероприятия')
sskb3 = KeyboardButton(text='Задать вопрос')

sskb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sskb_client.add(sskb1).add(sskb2).add(sskb3).add(kb_back)

# Задать вопросы
zvkb1 = KeyboardButton(text='Отправить')
zvkb2 = KeyboardButton(text='Назад')

zvkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
zvkb_client.add(zvkb1).add(zvkb2)

# Контакты
ka1 = KeyboardButton(text='Дублировать информацию')
ka2 = KeyboardButton(text='Отменить действие')

ka_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
ka_client.add(ka1).add(ka2)

#общаги
ob1 = KeyboardButton('№ 1')
ob2 = KeyboardButton('№ 2')
ob3 = KeyboardButton('№ 3')
ob4 = KeyboardButton('№ 4')
ob5 = KeyboardButton('№ 5')
ob6 = KeyboardButton('№ 6')
ob7 = KeyboardButton('№ 7')
ob8 = KeyboardButton('№ 8')
ob9 = KeyboardButton('№ 9')
ob10 = KeyboardButton('№ 10')
ob11 = KeyboardButton('№ 11')
ob12 = KeyboardButton('№ 12')
ob13 = KeyboardButton('№ 13')
ob14 = KeyboardButton('№ 14')
ob15 = KeyboardButton('№ 15')
ob16 = KeyboardButton('№ 16')
ob17 = KeyboardButton('№ 17')
ob18 = KeyboardButton('№ 18')
ob19 = KeyboardButton('№ 19')
ob20 = KeyboardButton('№ 20')
ob21 = KeyboardButton('№ 21')
ob22 = KeyboardButton('№ 22')
ob23 = KeyboardButton('№ 23')
ob24 = KeyboardButton('№ 24')
ob25 = KeyboardButton('№ 25')


obkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

obkb_client.add(ob1).insert(ob2).insert(ob4).add(ob5).insert(ob6).insert(ob7).add(ob8).insert(ob9).insert(ob10).add(ob11).insert(ob12).insert(ob13).add(ob14).insert(ob15).insert(ob16).add(ob17).insert(ob18).insert(ob19).add(ob20).insert(ob21).insert(ob22).add(ob23).insert(ob24).insert(ob25).add(kb_back)

base = sq.connect('basa.db')
cur = base.cursor()

i = cur.execute('SELECT dorm FROM dorms').fetchall()

obkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for j in range(25):
    if j%3 == 0:
        obkb_client.add(i[j][0])
    else:
        obkb_client.insert(i[j][0])

obkb_client.add(kb6)

