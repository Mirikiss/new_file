# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

# import os
# def splitting(h):
#     a, b = os.path.splitext(h)
#     c, d = os.path.split(a)
#     return  c, d, b
    
#     # n = os.path.split(h)
#     # return n[0], *n[1].split('.')
    

# text = 'H:\Exercise_python\Exercise_2\exercise_1.py'
# print(splitting(text))
import sys
from seminar_6 import find_number

if __name__ == '__main__':
    options = list(map(int, sys.argv[1:]))
    low_limit = 1
    high_limit = 100
    counter = 5
    if len(options) == 1:
        high_limit = options[0]
    elif len(options)== 2:
        low_limit, high_limit = options
    else:
        low_limit, high_limit, counter = options

find_number(low_limit, high_limit, counter)
