
#À l'aide de la inputfonction, demandez à l'utilisateur une chaîne. La chaîne doit comporter 10 caractères.

Caractere = input("Saisir un text : ")
taille = len(Caractere)
if taille<10:
    print(f"Chaine pas assez longue {taille}") #S'il contient moins de 10 caractères, imprimez un message indiquant "chaîne pas assez longue".
else:
    print(f"Chaine trop longue {taille}") #Si c'est plus de 10 caractères, imprimez un message indiquant "chaîne trop longue".

#À l' aide d'un for loop, construisez la chaîne caractère par caractère : imprimez le premier caractère, puis le deuxième, puis le troisième, jusqu'à ce que la chaîne complète soit imprimée. Par exemple:

print(f"le premier caractere est {Caractere[0]} et le dernier {Caractere[-1]}") #Ensuite, imprimez le premier et le dernier caractère du texte donné.


##À l' aide d'un for loop, construisez la chaîne caractère par caractère : imprimez le premier caractère, puis le deuxième, puis le troisième, jusqu'à ce que la chaîne complète soit imprimée. Par exemple:

for i in Caractere:
    print(i)

#Bonus : Échangez quelques caractères puis imprimez la nouvelle chaîne mélangée ( indice : regardez dans la shuffleméthode). Par exemple: