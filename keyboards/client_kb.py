from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sqlite3 as sq

kb_back = KeyboardButton('Назад')

# команды
# kb1 = KeyboardButton('Личный кабинет')
kb2 = KeyboardButton('Общежития')
kb3 = KeyboardButton('Студенческий совет')
kb4 = KeyboardButton('Задать вопрос')
kb5 = KeyboardButton('Полезное')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)  # замещает клавиатуру
kb_client.add(kb2).insert(kb3).add(kb4).insert(kb5)  # .add(kb1)

# Личный кабинет
'''
lkkb1 = KeyboardButton(text='Авторизация')
lkkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
lkkb_client.add(kb_back)#.add(lkkb1)
'''

# Студенческий совет
sskb1 = KeyboardButton(text='Кто мы?')
sskb2 = KeyboardButton(text='Группа ВК')

sskb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
sskb_client.add(sskb1).add(sskb2).add(kb_back)

# Задать вопросы
zvkb1 = KeyboardButton(text='Проживающим')
zvkb2 = KeyboardButton(text='Абитуриентам')
zvkb3 = KeyboardButton(text='Нет ответа?')
zvkb4 = KeyboardButton(text='Льготным категориям')

zvkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
zvkb_client.add(zvkb1).add(zvkb2).add(zvkb4).add(zvkb3).add(kb_back)

# Контакты
ka1 = KeyboardButton(text='Дублировать информацию')

ka_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
ka_client.add(ka1).add(kb_back)

# общаги

base = sq.connect('basa.db')
cur = base.cursor()

i = cur.execute('SELECT dorm FROM dorms').fetchall()

obkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
for j in range(21):
    if j % 3 == 0:
        obkb_client.add(i[j][0])
    else:
        obkb_client.insert(i[j][0])

obkb_client.add(kb_back)
base.close()

# Вопросы
base = sq.connect('basa.db')
cur = base.cursor()

i = cur.execute('SELECT Question FROM FAQ').fetchall()

liverskb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
for j in range(0, 4):
    liverskb_client.add(i[j][0])
liverskb_client.add(kb_back)

entrantskb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
for j in range(5, 13):
    entrantskb_client.add(i[j][0])
entrantskb_client.add(kb_back)

benefiterskb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
for j in range(14, 17):
    benefiterskb_client.add(i[j][0])
benefiterskb_client.add(kb_back)

base.close()


# Полезное
use_kb1 = KeyboardButton(text='Администрация СТГ')
use_kb2 = KeyboardButton(text='Центр поселения')
use_kb3 = KeyboardButton(text='Паспортный стол')

usekb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
usekb_client.add(use_kb1).insert(use_kb2).add(use_kb3).add(kb_back)
