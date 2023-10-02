class Cat:
    def __init__(self, name, age, habit):
        self.name = name
        self.age = age
        self.habit = habit
    
    def show_data(self):
        return f'{self.name} {self.age} age and  like {self.habit}!'

class Bird:
    def __init__(self, name, age, habit):
        self.name = name
        self.age = age
        self.habit = habit
    
    def show_data(self):
        return f'{self.name} {self.age} age and  like {self.habit}!'

class Dog:
    def __init__(self, name, age, habit):
        self.name = name
        self.age = age
        self.habit = habit
    
    def show_data(self):
        return f'{self.name} {self.age} age and  like {self.habit}!'

# part1 = Cat('Myrka', 5, 'sleep')
# part2 = Bird('Kesha', 2, 'fly')
# part3 = Dog('Palcan', 10, 'bark')

# print(part1.show_data())
# print(part2.show_data())
# print(part3.show_data())

class Animale:
    def creat_animale(self, animale_type, name, age, habit):
        if animale_type.lower() == 'cat':
            return Cat('Myrka', 5, 'sleep')
        elif animale_type.lower() == 'dog':
            return Dog('Palcan', 10, 'bark')
        elif animale_type.lower() == 'bird':
            return Bird('Kesha', 2, 'fly')
        else:
            raise ValueError('Такого нет')

#ani = Animale()

cat = Animale().creat_animale('Cat', 'Myrka', 5, 'sleep')
# dog = ani.creat_animale('Dog', 'Palcan', 10, 'bark')
# bird = ani.creat_animale('Bird', 'Kesha', 2, 'fly')
#carrot = ani.creat_animale('carrot', 5, 5, 5)

print(cat.show_data())
# print(dog.show_data())
# print(bird.show_data())
#print(carrot.show_data()) для вызова ошибки