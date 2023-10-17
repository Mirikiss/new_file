class User:

    def __init__(self, name:str, equiment: list = None):
        self.name = name
        self.equiment = equiment if  equiment is not None else []
        self.live = 3

    def __str__(self):
        eq = 'оборудование: ' + ', '.join(self.equiment) if self.equiment else 'пусты руки' 
        return f' Имя {self.name} с {eq} жизни {self.live}'   

    def __repr__(self):
        return f'Name {self.name} or {self.equiment}'
    
part1 = User('Сплингер', ["пистолет", 'нож'])

print(part1)
