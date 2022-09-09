#Exercice 1

Liste1 = [1,2,3,4]
Liste2 = [5,6,7,8]
Liste1.extend(Liste2)
print(Liste1)

#Exercice 2

#Créez une boucle qui va de 1500 à 2500 et imprime tous les multiples de 5 et 7.
Listes = [i for i in range(1500, 2500+1) if i%5==0 if i%7==0]
print(Listes)

#Exercice 3

#Demander son nom à un utilisateur, si son nom est dans la liste des noms imprimer l'index de la première occurrence du nom.

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

userLastName = input("Quelle est votre nom ? ")
if userLastName in names:
    rang = names.index(userLastName)
    print(f"votre nom est à l'index {rang}")
else:
    print("Votre n'est pas dans la liste ")

# Exercice 4

#Demandez à l'utilisateur 3 chiffres et imprimez le plus grand nombre.

Ensemble = list()

N1 = int(input("Nombre 1 : "))
Ensemble.append(N1)
N2 = int(input("Nombre : 2 "))
Ensemble.append(N2)
N3 = int(input("Nombre 3 : "))
Ensemble.append(N3)
print(f"Le plus grand est : {max(Ensemble)}")

# Exercice 5

#Créer une chaîne de toutes les lettres de l'alphabet
#Faites une boucle sur chaque lettre et imprimez un message qui contient la lettre et si c'est une voyelle ou une consonne.

chaine = "abcdefghijklmnopqrstuvwxyz"
voyelle = "aeiouy"
message = "je suis present"
for lettre in chaine:
    if lettre in message:
        if lettre in voyelle:
            print("voyelle")
        else:
            print("consomme")


#Exercicie 6

listeMots = list()
for i in range(1,8):
    words = input("Entrer sept :")
    listeMots.append(words)
print(listeMots)
car = input("Saisir un caractère : ")
for lettre in listeMots:
    if car in lettre:
        print(f"{car} est à la position : {lettre.index(car)} du mot : {lettre}")
    else:
        print(f"La lettre {car} n'existe pas dans aucun mot")


#Exercicie 7

#Créez une liste de nombres de un à un million, puis utilisez min()et max()pour vous assurer que votre liste commence réellement à un et se termine à un million. Utilisez la sum()fonction pour voir à quelle vitesse Python peut ajouter un million de nombres.

Liste = [i for i in range(1,1000000+1)]
print(f"Le minimum de la liste est {min(Liste)}, le maximun de la liste est {max(Liste)} et la somme est {sum(Liste)}")

#Exercicie 8

#Écrivez un programme qui accepte une séquence de nombres séparés par des virgules. Générez une liste et un tuple contenant chaque nombre.

Entree = input("Saisir le nombre separeré par des virgules :")
Listes = Entree.split(',')
#Convert using map int and tuple
Tuples = tuple(map(int, Entree.split(',')))
print(Listes)
print(Tuples)

#ou

Entree = input("Saisir le nombre separeré par des virgules :")
Listes = Entree.split(',')
#conert using eval method
Tuples = eval(Entree)
print(Listes)
print(Tuples)

#Exercicie 9

import random
from random import randint
competeur = 0
while True:
    nombreEngtre = int(input("Veillez saisir le nombre mistere : "))
    nombreMistere = randint(1, 2)
    if nombreEngtre==nombreMistere:
        competeur = +1
        print(f"bravo vous avez gagnez en {competeur} coups")
    else:
        print(f"Le resultat est {nombreMistere} veillez essayer")
    competeur = +1
print(f"Vous avez perdu {competeur} fois ")