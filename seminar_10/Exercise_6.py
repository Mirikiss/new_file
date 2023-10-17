class Animals:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Fish(Animals):
    
    def __init__(self, name, age, specificity):
        super().__init__(name, age)
        self.specificity = specificity

    def show_info(self):
        return f'Умение: {self.specificity}'

class Bird(Animals):
    
    def __init__(self, name, age, specificity):
        super().__init__(name, age)
        self.specificity = specificity
    
    def show_info(self):
        return f'Умение: {self.specificity}'

bird = Bird('Кеша', 7, 'летает')
fish = Fish('Немо', 2, 'плавает')

print(bird.show_info())
print(fish.show_info())