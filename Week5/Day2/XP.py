class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

class Siamese(Cat):
    pass

cat1 = Bengal('chici', 2)
cat2 = Chartreux('chaci', 3)
cat3 = Siamese('checi', 8)
all_cats = [cat1, cat2, cat3]
sara_pets = Pets(all_cats)
sara_pets.walk()

#Exercice 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self, name):
        print(self.name, 'aboie')
        
    def run_speed(self, age, weight):
        return self.weight/(self.age*10)
    
    def fight(self, other_dog):
        if self.run_speed(self.age, self.weight) > other_dog.run_speed(self.age, self.weight):
            print(f'{self.name} a gagné')
        else :
            print(f'{other_dog.name} a gagné')

dog1 = Dog('Confiance',8,50)
dog2 = Dog('Dodo',7,75)
dog3 = Dog('Pitou',6,20)

print(f'{dog1.run_speed(7, 75)} m/s.')
dog2.fight(dog3)