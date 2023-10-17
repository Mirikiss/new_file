import time
from datetime import datetime

class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"

event = MyStr("Завершилось тестирование", "John")
print(event)