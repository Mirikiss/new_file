# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.


def number():
    while True:
        try:
            num = input()
            num = float(num)
            return int(num) if int(num) == num else num
        except:
            raise ValueError('Не верный данные')
# print(number())

if __name__ == '__main__':
    print(number())