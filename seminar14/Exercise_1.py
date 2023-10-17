# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_lowercase
import doctest

def clear_case(text):
    '''
    >>> clear_case('text') == 'text'
    True
    >>> clear_case('text') == 'te..xt'
    Flase
    >>> clear_case('te xt') == 'te xt'
    True
    >>> clear_case('text') == 'te//xt'
    True    
    '''
    result = ''
    if text is not None:
        for i in text:
            if i.lower() in ascii_lowercase + ' ':
                result += i
        return result.lower()
    raise  ValueError('fsdfsdfsdf')

if __name__ == '__main__':
    doctest.testmod(verbose=True)

