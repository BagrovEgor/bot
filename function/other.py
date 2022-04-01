from dop import dp, bot
from aiogram import Dispatcher, types


# в message будет находиться все, что вернет нам телега после получения сообщения
# await - чтобы асинхронно подождать, то есть ответ, когда будет свободное время, то ответ
# как только боту придет сообщение, будет срабатывать функция echo
async def echo_send(message: types.Message):  # async чтобы не простаивало свободное время
    if message.text == 'привет':
        await bot.send_message(message.from_user.id, 'Привет')

def register_handlers_other(dp: Dispatcher):  # аннотация типов
    dp.register_message_handler(echo_send)
