# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class MyExeption(Exception):

    def __init__(self, msg):
        self.messag = msg

    def __str__(self):
        return f'Моё исключение:  {self.messag}'
    
class LevelError(MyExeption):
    def __init__(self, msg):
        super().__init__(msg)

class AssertionError(MyExeption):
    def __init__(self, msg):
        super().__init__(msg)

print(AssertionError('ошиба доступа'))
