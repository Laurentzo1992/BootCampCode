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