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
base.close()

# Инфа об общагах
inf_dorm1 = KeyboardButton(text='Администрация')
inf_dorm2 = KeyboardButton(text='Адрес')
inf_dorm3 = KeyboardButton(text='Мероприятия в общежитии')
inf_dorm4 = KeyboardButton(text='Вконтакте')
inf_dorm5 = KeyboardButton(text='Instagram')
inf_dorm6 = KeyboardButton(text='Отменить действия')

infkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

infkb_client.add(inf_dorm1).add(inf_dorm2).add(inf_dorm3).add(inf_dorm4).add(inf_dorm5).add(inf_dorm6)
