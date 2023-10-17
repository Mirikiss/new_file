# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return round(self.radius **2 * pi, 2)
    
    def longth_cirlce(self):
        return round(self.radius * 2 * pi, 2)

part1 = Circle(4)

print(part1.longth_cirlce())
print(part1.square())




        