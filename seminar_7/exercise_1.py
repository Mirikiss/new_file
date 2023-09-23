# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции

import random

def numbers_random(number):
    i = 0
    while i <= number:
        ran_int = random.randint(-1000, 1000)
        ran_float = random.uniform(-1000, 1000)
        with open('file_number.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{ran_int}|{ran_float}\n')
        i+=1
    

    


print(numbers_random(int(input('введите количество добавляемых чисел: '))))