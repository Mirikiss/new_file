# 📌Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Dog():
    def __init__(self, name, age, command = 'run'):
        self.name = name
        self.age = age
        self.command = command

    def show_info(self):
            return f'{self.name}  can {self.command}'
    
class Cat():
    def __init__(self, name, age, sleep_time):
        self.name = name
        self.age = age
        self.sleep_time = sleep_time

    def show_info(self):
        return f'{self.sleep_time} {self.name}'

class Bird():
    def __init__(self, name, age, sign_power):
        self.name = name
        self.age = age
        self.sign_power = sign_power

    def show_info(self):
            return f'{self.sign_power} {self.name}'
    
a = Dog('Bob', 5)
print(a.show_info())
b = Cat('San', 6, 'sleep')
print(b.show_info())
c = Bird('kuk', 7, 'Fly')
print(c.show_info())