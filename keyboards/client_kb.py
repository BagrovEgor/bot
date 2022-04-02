from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# команды
kb1 = KeyboardButton('Личный кабинет')
kb2 = KeyboardButton('Общежития')
kb3 = KeyboardButton('Студенческий совет')
kb4 = KeyboardButton('Задать вопросы')
kb5 = KeyboardButton('Контакты')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # замещает клавиатуру
kb_client.add(kb1).add(kb2).insert(kb3).add(kb4).insert(kb5)


lkkb1 = KeyboardButton(text='Регистрация')
lkkb2 = KeyboardButton(text='Выход')

lkkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
lkkb_client.add(lkkb1).add(lkkb2)
