# Создайте функцию генератор чисел Фибоначчи 




def gen_fibonachi(n):
    a = b = 1
    for _ in range(n):
            yield a
            a, b = b, a + b
n = int(input('Сколько чисел Фибоначчи вывести: '))

for i in gen_fibonachi(n):
      print(i, end = ' ')

