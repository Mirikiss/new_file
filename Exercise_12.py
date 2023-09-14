# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os
def splitting(h):
    a, b = os.path.splitext(h)
    c, d = os.path.split(a)
    return  c, d, b
    
    # n = os.path.split(h)
    # return n[0], *n[1].split('.')
    

text = 'H:\Exercise_python\Exercise_2\exercise_1.py'
print(splitting(text))
      