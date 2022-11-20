# Mode D'emploi : Ancienne Ferme MacDonald
class Ferme:
    def __init__(self, nom):
        self.nom = nom
        self.animal = {}

    def add_animal(self, nom, nombre=1):
        if nom in self.animal :
            self.animal.update({nom : self.animal[nom]+nombre})
        else :
            self.animal.update({nom : nombre})

    def get_info(self) :
        mot = ""
        print(f"{self.nom}'s farm\n")
        for x in self.animal :
            mot += x + " : " + str(self.animal[x]) + "\n"
        mot += ""
        return mot

    def get_animal_types(self) :
        animal = []
        for x in self.animal :
            animal.append(x)
        return sorted(animal)

    def get_sort_info(self) :
        mot = "\nMcDonald’s ferme has "
        animal = self.get_animal_types()
        for i in range(0,len(animal)) :
            if i == len(animal)-1 :
                mot += animal[i] + "."
            elif i == len(animal)-2 :
                mot += animal[i] + " and "
            else :
                mot += animal[i] + ", "
        return mot


macdonald = Ferme("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_sort_info())

        
