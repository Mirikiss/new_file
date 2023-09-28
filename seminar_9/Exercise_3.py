# 📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# 📌У класса должны быть методы birthday для увеличения возраста на год, 
# full_name для вывода полного ФИО и т.п. на ваш выбор. 
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

class Circle:
    def __init__(self, surname, age):
        self.surname = surname
        self.age = age
    
    def  birthday(self):
        self.age += 1
    
    def show_age(self):
        return f'{self.surname} {self.age}'
    
    def show_name(self):
        return self.surname

a = Circle('Заяц', 18)
print(a.show_age())
a.birthday()
print(a.show_age())
