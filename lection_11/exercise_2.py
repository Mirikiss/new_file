class User:

    def __init__(self, name:str):
        self.name = name
        print(f'Creat {self.name = }')

    def __repr__(self):
        return f'Name {self.name}'
    
part1 = User('Сплингер')

print(part1)
