class User:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'верх {self.x} низ {self.y}'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return User(x, y)

    
part1 = User(2, 4)
part2 = User(3, 7)
part3 = part1 + part2
print(part3)
