# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import os
import json

class User:
    
    def __init__(self, name: str, the_id: int, level: int):
        #if not isinstance(name, str) and name.isalpha():
            #raise ValueError('Имя должно быть тестом')
        self.name = name
        #if not isinstance(the_id, int):
            #raise ValueError('ид должно быть числом')
        self.the_id = the_id
        #if not isinstance(the_id, int):
            #raise ValueError('уровегь  должн быть числом')
        self.level = level

        def __str__(self):
            return f'{self.name = } - {self.the_id = } - {self.level = }'
    
def load_json():
    if os.path.exists(PATH_DB):
        with open(PATH_DB, r, encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data




def Worker():
    while True:
        try:
            name = input('Введите имя: ')
            the_id = int(input('номер: '))
            level = int(input('левел персонажа: '))
            return User(name, the_id, level)
        except ValueError as e:
            raise e
        
if __name__ == '__main__':
    print(Worker())






