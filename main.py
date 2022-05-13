# bot - это класс, к которому мы обращаемся для отправки сообщений
# types - для работы с сообщением, данными от нлайновых кнопок и т.д.
# Dispatcher - класс, на основе которого создадим объект, нужен для создание хэндлеров (работы с событиями)
# executor - для поллинга, т е чтобы бот работал постоянно


from aiogram.utils import executor
from dop import dp

from function import client, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp)  # чтобы бот работал постоянно
