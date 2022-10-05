# Exercice 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Pipi", 2)
cat2 = Cat("Pipo", 5)
cat3 = Cat("Pepu", 4)

def chatEncein():
    cat = [cat1, cat2, cat3]
    print(f"Le chat le plus âgé est , et a ans.")
    print(cat)
    return cat 
chatEncein()



