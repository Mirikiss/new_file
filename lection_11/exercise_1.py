class User:

    def __init__(self, name:str):
        self.name = name
        print(f'Creat {self.name = }')

    def __new__(cls, *args, **kwars):
        instance = super().__new__(cls)
        print(f'creat {cls}')
        return instance
    
part1 = User('Сплингер')
part2 = User('лщдд')
