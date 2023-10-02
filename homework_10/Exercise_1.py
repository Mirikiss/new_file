# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра.
class Animale():
     def __init__(self, name_animale, age, habit):
          self.name_animale = name_animale
          self.age = age
          self.habit = habit
          self.spec = None


     def get_spec(self):
          return self.spec
     
class Cat(Animale):
    def __init__(self, name_animale, age, habit, spec):
         super().__init__(name_animale, age, habit)
         self.spec = spec       
          
# class Cat():
#     def __init__(self, name_animale, age,  habit):
#          self.name_animale = name_animale
#          self.age = age
#          self.habit = habit

    def show_info(self):
         return f'{self.name_animale} {self.age} любит {self.habit}'
    
class Dog():
    def __init__(self, name_animale, age,  habit):
         self.name_animale = name_animale
         self.age = age
         self.habit = habit

    def show_info(self):
         return f'{self.name_animale} {self.age} любит {self.habit}'


class Bird():
    def __init__(self, name_animale, age,  habit):
         self.name_animale = name_animale
         self.age = age
         self.habit = habit

    def show_info(self):
         return f'{self.name_animale} {self.age} любит {self.habit}'
    
# a = Dog('Барсик', 7, 'лаять')
# b = Bird('Кеша', 3, 'летать')
# c = Cat('Мурка', 11, 'спать')
# k = (a, b, c)
# for i in (a, b, c):
#      print(i.show_info())

class factory:
    def creat_animale(self, animale_type, name_animale, age, habit):
         if animale_type.lower() == 'cat':
              return Cat(name_animale, age,  habit)
         elif animale_type.lower() == 'dog':
              return Dog(name_animale, age,  habit)
         elif animale_type.lower() == 'bird':
              return Bird(name_animale, age,  habit)
         else:
              raise ValueError("Invalid animal type")
         
fact = factory()

cat = fact.creat_animale('cat', 'Мурка', 11, 'спать')
dog = fact.creat_animale('dog', 'Барсик', 7, 'лаять')
bird = fact.creat_animale('bird', 'Кеша', 3, 'летать')

print(cat.get_spec())
# print(bird.show_info())
# print(dog.show_info())



