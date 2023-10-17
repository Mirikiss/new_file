# 📌Создайте функцию, которая удаляет из текста все 
# символы кроме букв латинского алфавита и пробелов. 
# 📌Возвращается строка в нижнем регистре.

import doctest
from string import ascii_lowercase
def clear_text(test:str):
    '''
    >>> clear_text('text') == 'text'
    True
    '''
    result = ''
    for i in test:
        if i in ascii_lowercase + ' ':
            result += i
    return result.lower()

if __name__ == '__main__':
    doctest.testmod(verbose=True)
