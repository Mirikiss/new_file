# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

from datetime import datetime
class My_Str(str):

    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.creat_time = datetime.now()
        return instance

    # def __init__(self, author, value):
    #     self.author = author
    #     self.value = value
    #     self.creat_time = datetime.now()


part = My_Str('tut', 'nun')
print(part)

    