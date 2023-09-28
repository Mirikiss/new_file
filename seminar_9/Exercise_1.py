# 📌Создайте класс окружность.
# 📌Класс должен принимать радиус окружности при создании экземпляра. 
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi

class Circle:

    def __init__(self, rnd):
        self.rnd = rnd

    def length(self):
        return 2*self.rnd*3.14
    
    def area(self, rnd):
        return (self.rnd * self.rnd)* pi
    
a = Circle(5)
print(a.length())
print(a.area())

