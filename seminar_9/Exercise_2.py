# 📌Создайте класс прямоугольник. 
# 📌Класс должен принимать длину и ширину при создании экземпляра. 
# 📌У класса должно быть два метода, возвращающие периметр и площадь. 
# 📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Circle:

    def __init__(self, lenght, weidth = None):
        self.lenght = lenght
        self.weidth = weidth if weidth else lenght

    def length(self):
        return 2*self.rnd*3.14
    
    def area(self, rnd):
        return (self.rnd * self.rnd)* pi
    
a = Circle(5)
print(a.length())
print(a.area())
