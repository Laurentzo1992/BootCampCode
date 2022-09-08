#Exercice 1

my_fav_numbers.add(11)
print(my_fav_numbers)
#Suprimer le dernier numero
my_fav_numbers.discard(11)
print(my_fav_numbers)
# ensemble des numero d'un amis
friend_fav_numbers = {12, 13, 14, 15, 16, 17, 18, 19, 20}
#union de nos numero favoris
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercicie 2
#Reponse non les tuple sont immuable

#Exercice 3

basket = ["Banana", "Apples", "Oranges", "Blueberries", "Blueberries", "Myrtilles "];
print(basket)
#Suprimer Banana
basket.remove("Banana")
print(basket)
#Suprimer le deernier element
basket.pop()
print(basket)
#Ajouter Kiwi à la fin
basket.append("Kiwi")
print(basket)
# Ajouter Pommes au debut
basket.insert(0,"Pommes")
print(basket)
#Compter le nombre de Pommes
print(basket.count("Pommes"))
#Netoyer la liste
basket.clear()
#Afficher la liste
print(basket)


#Exercice 4

#un entier est un type de donnée numerique sans virgule flotante et que le float est un type de donnée numerique avec virgule flotante

#Pouvez-vous penser à une autre façon de générer une séquence de flottants ?
#Oui en utilisant une boucle 
Liste = []
for i in range(3, 11):
    elmentList = i/2
    Liste.append(elmentList)
print(Liste)


#Exercice 5
#Utilisez une for boucle pour imprimer tous les nombres de 1 à 20 inclus.
for i in range(1,21):
    print(i)
#En utilisant une forboucle, qui boucle de 1 à 20 (inclus), imprimez chaque élément qui a un index pair.
for i in range(1,21):
    if i%2==0:
        print(i)

#Exercice 6

nom = "Laurent"
while True:
    s = input('Enter votre nom : ')
    if s == nom:
        break
    print("Incorrect saisir votre")
print(f"Merci votre nom est {nom}")

#Exercice 7

s = input("Veillez saisir une liste de fruits separé par des spaces : ")
maListe = s.split(" ")
favorit = input("veillez saisir votre fruits favoris : ")
if favorit in maListe:
    print(f"votre fuits prefere est {favorit}")
else:
    print("You chose a new fruit. I hope you enjoy")

#Exercice 8
#Écrivez une boucle qui demande à un utilisateur d'entrer une série de garnitures de pizza, lorsque l'utilisateur saisit "quitter", arrêtez de demander des garnitures.
#Au fur et à mesure qu'ils entrent dans chaque garniture, imprimez un message indiquant que vous ajouterez cette garniture à leur pizza.
#À la sortie de la boucle, imprimez toutes les garnitures sur la pizza et quel est le prix total (10 + 2,5 pour chaque garniture).

pizza = []
somme = 0
while True:
    Enter = input("Saisir les garnitures pour alilenter votre Pizza ou tapez quit pour sortir : ")
    pizza.append(Enter)
    print("Votre ganiture a été ajouter à votre pizza")
    if Enter == "quit":
        print("Merci pour vos ajout")
        break
    somme = len(pizza)*(12.5)
print(f" votre pizza est commosé de {pizza} au Prix total de : {somme}$")