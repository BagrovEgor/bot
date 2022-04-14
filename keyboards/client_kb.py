from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# команды
kb1 = KeyboardButton('Личный кабинет')
kb2 = KeyboardButton('Общежития')
kb3 = KeyboardButton('Студенческий совет')
kb4 = KeyboardButton('Задать вопросы')
kb5 = KeyboardButton('Контакты')
kb6 = KeyboardButton('Отменить действие')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # замещает клавиатуру
kb_client.add(kb1).add(kb2).insert(kb3).add(kb4).insert(kb5).add(kb6)

# Личный кабинет
lkkb1 = KeyboardButton(text='Регистрация')
lkkb2 = KeyboardButton(text='Выход')

lkkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
lkkb_client.add(lkkb1).add(lkkb2).add(kb6)

# Студенческий совет
sskb1 = KeyboardButton(text='Информация')
sskb2 = KeyboardButton(text='Мероприятия')
sskb3 = KeyboardButton(text='Задать вопрос')
sskb4 = KeyboardButton(text='Отменить действие')

sskb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sskb_client.add(sskb1).add(sskb2).add(sskb3).add(sskb4)

# Задать вопросы
zvkb1 = KeyboardButton(text='Отправить')
zvkb2 = KeyboardButton(text='Отменить действие')

zvkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
zvkb_client.add(zvkb1).add(zvkb2)

#общаги
ob1 = KeyboardButton('1')
ob2 = KeyboardButton('2')
ob3 = KeyboardButton('3')
ob4 = KeyboardButton('4')
ob5 = KeyboardButton('5')
ob6 = KeyboardButton('6')
ob7 = KeyboardButton('7dor')
ob8 = KeyboardButton('8dor')
ob9 = KeyboardButton('9-ая')
ob10 = KeyboardButton('10-ая')
ob11 = KeyboardButton('11-ая')
ob12 = KeyboardButton('12-ая')
ob13 = KeyboardButton('13-ая')
ob14 = KeyboardButton('14-ая')
ob15 = KeyboardButton('15-ая')
ob16 = KeyboardButton('16-ая')
ob17 = KeyboardButton('17-ая')
ob18 = KeyboardButton('18-ая')
ob19 = KeyboardButton('19-ая')
ob20 = KeyboardButton('20-ая')
ob21 = KeyboardButton('21-ая')
ob22 = KeyboardButton('22-ая')
ob23 = KeyboardButton('23-ая')
ob24 = KeyboardButton('24-ая')
ob25 = KeyboardButton('25-ая')


obkb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

obkb_client.add(ob1).insert(ob2).insert(ob4).add(ob5).insert(ob6).insert(ob7).add(ob8).insert(ob9).insert(ob10).add(ob11).insert(ob12).insert(ob13).add(ob14).insert(ob15).insert(ob16).add(ob17).insert(ob18).insert(ob19).add(ob20).insert(ob21).insert(ob22).add(ob23).insert(ob24).insert(ob25).add(kb6)