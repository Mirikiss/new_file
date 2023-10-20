# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль

import logging

logger = logging.getLogger(__name__)

format = '{asctime:<20} - {levelname:<10} - {msg}'

logging.basicConfig(filename='mylog.log', filemode = 'w', encoding='utf-8',
                    level=logging.ERROR, style='{', format = format )


def zero(a: int, b: int):
    try:
        return a/b
    except ZeroDivisionError as e:
        logging.error(msg = e)




zero(5, 0)
