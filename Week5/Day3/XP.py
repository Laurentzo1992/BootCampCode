#Exercice 1
class Documentation:
    
    def __init__(self):
        chiffre = input("Saisir un chiffre : ")
        chiffre = int(chiffre)
        print(abs(chiffre))
        print(chiffre)
        
    def __doc__(self):
        return "Documantation du programe"
    
Doc = Documentation()
print( Doc.__doc__())

#Exercice 2

class Currency:
	
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount > 1 :
            return f"{self.amount} {self.currency}s"
        else :
            return f"{self.amount} {self.currency}"

    def __repr__(self):
        if self.amount > 1 :
            return f"{self.amount} {self.currency}s"
        else :
            return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        a=True
        try :
            if self.currency == other.currency :
                print(self.amount + other.amount)
                return Currency(self.currency,self.amount + other.amount)
            else :
                a=False
        except :
            if a :
                print(self.amount + other)
                return Currency(self.currency,self.amount + other)
        if not a :
            raise TypeError("Cannot add between Currency type <dollar> and <shekel>")


