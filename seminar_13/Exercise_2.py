# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def func(s:dict, key, default = 'Нет такого'):
    try:
        return s[key]
    except KeyError as s:
        return  default

if __name__ == '__main__':
    my_dict = {1: 'Один'}
    print(func(my_dict, 2, 'Другое'))  