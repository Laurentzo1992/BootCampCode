#Exercice 1 deux

#Demandez à l'utilisateur un numberet un length.
#Créez un programme qui imprime une liste de multiples de numberjusqu'à ce que la longueur de la liste atteigne length.

number = int(input("Entrer un nombre : "))
length = int(input("Entrer une taille en nombre : "))
Liste = []
while len(Liste)<=length:
    if number%number==0 and number%1==0:
        Liste.append(number)
        number+=number
    if len(Liste)==length:
        break
print(Liste)

#Exercicie 2

#Écrivez un programme qui demande une chaîne à l'utilisateur et affichez une nouvelle chaîne avec toutes les lettres consécutives en double supprimées.

newChaine = input("Veillez saisir une phrase : ")
chaine = set(newChaine)
print(f"Phrase entrée : {newChaine}")
print(f"votre phrase sans doublons {chaine}")
