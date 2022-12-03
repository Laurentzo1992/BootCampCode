class Family:

    def __init__(self,last_name):
        self.last_name = last_name
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]

    def born(self, **kwargs):
        info = {
        }
        for x in kwargs:
            info.update({x : kwargs[x]})
        self.members.append(info)

    def is_18(self,name):
        for memb in self.members:
            if name == memb['name']:
                if memb['age'] > 18:
                    return True
                else:
                    return False
        return False

    def family_presentation(self):
        print(self.last_name)
        i = 1
        for membre in self.members:
            print(i,":",membre['name'])
            i+=1

fama = Family("SAWADOGO")
fama.born(name = 'Sss', age = 15, gender = 'Male', is_child=True)
fama.born(name = 'Sah', age = 2, gender = 'Female', is_child=True)
print(fama.is_18('Sarah'))
print(fama.is_18('Sah'))
fama.family_presentation()

# Exercice 2 : La Famille Des Indestructibles

class TheIncredibles(Family):
    def __init__(self,lastname):
        super().__init__(lastname)
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
             'incredible_name': 'MikeFly'},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
             'incredible_name': 'SuperWoman'}
        ]
    def use_power(self, name):
        for membre in self.members:
            if name == membre['name']:
                if membre['age'] > 18:
                    print(f"{membre['power']}")
                else :
                    raise Exception(f"{name} n'a pas plus de 18 ans")
            else:
                print(f"{name} n'est pas membre de cette famille")

    def incredible_presentation(self):
        super().family_presentation()
        print('\nChaque membre à comme pouvoir : ')
        i = 1
        for membre in self.members:
            print(i,':',membre['power'])
            i += 1

fama = TheIncredibles("NARE")
fama.born(name = 'Jack', age = 5, gender = 'Male', is_child=True, power = 'Unknown Power', incredible_name= 'Baby')
fama.born(name = 'Marie', age = 15, gender = 'Female', is_child=True, power = 'Speak to animals', incredible_name= 'SuperWoman')
fama.incredible_presentation()



