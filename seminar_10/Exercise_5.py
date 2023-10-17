# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

#                   №5
class Fish:
    
    def __init__(self, name, age, specificity):
        self.name = name
        self.age = age
        self.specificity = specificity

    def show_info(self):
        return f'Умение: {self.specificity}'

class Bird:
    
    def __init__(self, name, age, specificity):
        self.name = name
        self.age = age
        self.specificity = specificity
    
    def show_info(self):
        return f'Умение: {self.specificity}'


bird = Bird('Кеша', 7, 'летает')
fish = Fish('Немо', 2, 'плавает')

print(bird.show_info())
print(fish.show_info())
