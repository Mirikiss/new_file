# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.





class Person:

    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age
        self.last_name= last_name

    def birthday(self):
        self.age = self.age + 1
    
    def full_name(self):
        return f'{self.name} {self.last_name} - {self.age} age!'

part = Person('Pavel', 18, 'Aleksandov')

print(part.full_name())
part.birthday()
print(part.full_name())

# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

class Worker(Person):
    def __init__(self, name, age, last_name, number_id):
        super().__init__(name, age, last_name)
        self.number_id = sum(list(map(int, number_id))) % 7
wok = Worker('Pavel', 18, 'Aleksandov', '12345671')


print(wok.number_id)
