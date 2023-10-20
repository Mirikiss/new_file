# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging
from typing import Callable
from functools import wraps

def decor(func: Callable):
    logger = logging.getLogger(__name__)
    my_format = '{msg}'
    logging.basicConfig(filename='my_log.log', filemode='a', encoding='utf-8',
                         level = logging.INFO, style='{', format=my_format)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'result: {result}, args {args}, kwargs {kwargs}')
        return result
    return wrapper

@decor
def sum_func(a, b):
    return a + '_' + b

sum_func('первая', 'вторая')