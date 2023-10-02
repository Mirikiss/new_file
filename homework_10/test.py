class Animale():
     def __init__(self, name_animale, age, habit):
          self.name_animale = name_animale
          self.age = age
          self.habit = habit
          self.spec = None

     def get_spec(self):
          return self.spec
     
class Cat(Animale):
    def __init__(self, name_animale, age, habit, spec):
         super().__init__(name_animale, age, habit)
         self.spec = spec       
          


class factory:
    def creat_animale(self, animale_type, name_animale, age, habit):
         if animale_type.lower() == 'cat':
              return Cat(name_animale, age,  habit)
         elif animale_type.lower() == 'dog':
              return Dog(name_animale, age,  habit)
         elif animale_type.lower() == 'bird':
              return Bird(name_animale, age,  habit)
         else:
              raise ValueError("Invalid animal type")
         
fact = factory()

cat = fact.creat_animale('cat', 'Мурка', 11, 'спать')