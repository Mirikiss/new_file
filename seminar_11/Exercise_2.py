class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self.width + self._height)

    def area(self):
        return self.width * self._height

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self._height}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self._height})"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Так нельзя')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('Так нельзя')
        self._height = value

r1 = Rectangle(1, 2)
r1.width = -1