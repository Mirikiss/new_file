# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random
import string

latter = string.ascii_lowercase
latter_gls = 'aoyiue'

def generasion_name():
    size = random.randint(4, 6)
    name = random.sample(latter, size)
    name.append(random.choice(latter_gls))
    random.shuffle(name)
    name = ''.join(name).title()
    return name

def counter_name(counter):
    with open('generasion_name.txt', 'a+', encoding='utf-8') as file:
        for _ in range(counter):
            file.write(f'{generasion_name()}\n')

print(counter_name(int(input())))
