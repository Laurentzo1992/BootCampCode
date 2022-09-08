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


#Exercice 9

#Une salle de cinéma facture des prix de billets différents en fonction de l'âge d'une personne.
# si une personne a moins de 3 ans, le billet est gratuit.
# s'ils sont entre 3 et 12, le billet est de 10 $.
# s'ils ont plus de 12 ans, le billet est de 15 $.
# Demandez à une famille l'âge de chaque personne qui veut un billet.
# Enregistrez le coût total de tous les billets de la famille et imprimez-le.

nombrepersonneAge10 = 0
nombrepersonneAge12 = 0
prixTotal = 0
while True:
    age = int(input("Veillez indiquer votre age svp taper -1 pour sortir : "))
    if age == -1:
        break
    else:
        if age > 0 and age < 3:
            print("Le ticket est gratuit")
        elif age >= 3 and age <= 12:
            print("prix du ticket 10$")
            nombrepersonneAge10 = +1
        else:
            print("Prix du ticket 15$")
            nombrepersonneAge12 = +1
        prixTotal = (nombrepersonneAge10 * 10) + (nombrepersonneAge12 * 12)
    if age ==-1:
        break
print(f"Prix total est {prixTotal}")

# Un groupe d'adolescents vient dans votre salle de cinéma et souhaite regarder un film réservé aux personnes âgées de 16 à 21 ans.
# Compte tenu d'une liste de noms, écrivez un programme qui demande à l'adolescent son âge, s'il n'est pas autorisé pour regarder le film, supprimez-les de la liste.
# À la fin, imprimez la liste finale.

Liste = []
while True:
    Entr = input("Entrer le nom dans la liste ou tapez quit pour quitter: ")
    Liste.append(Entr)
    print(f"Liste initaile {Liste} ")
    if Entr == "quit":
        break
    else:
        for nom in Liste:
            elementAge = input("Age svp : ")
            if elementAge <= 16 and elementAge >= 21:
                print("Autoriser")
            else:
                Liste.remove(nom)
print(f" Liste finale {Liste}")


#Exercice 10
# Utilisez la liste ci-dessus appelée sandwich_orders.
# Créez une liste vide appelée finished_sandwiches.
# Au fur et à mesure que chaque sandwich est préparé, déplacez-le vers la liste des sandwichs finis.
# Une fois que tous les sandwichs ont été préparés, imprimez un message répertoriant chaque sandwich qui a été préparé , tel que I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while sandwich_orders != []:
    for sandwich in sandwich_orders:
        Entr = int(input(f"Dites si le sandwich {sandwich }est pret en tapant 1 :"))
        if Entr == 1:
            finished_sandwiches.append(sandwich)
            sandwich_orders.remove(sandwich)
            print(f"{sandwich} est près ")
    print(f"Votre menu tout près : {finished_sandwiches}")
    print(f"Il reste {sandwich_orders} non cuit ")


#Exercice 11


# En utilisant la liste sandwich_ordersde l'exercice précédent, assurez-vous que le sandwich 'pastrami' apparaît dans la liste au moins trois fois.
# Ajoutez du code au début de votre programme pour imprimer un message indiquant que la charcuterie n'a plus de pastrami, puis utilisez une whileboucle pour supprimer toutes les occurrences de 'pastrami' de sandwich_orders.
# Assurez-vous qu'aucun sandwich au pastrami ne se retrouve dans finished_sandwiches.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print("Il y a plus Pastrami sandwich")
while sandwich_orders:
    if "Pastrami sandwich" in sandwich_orders:
        sandwich_orders.remove("Pastrami sandwich")
    else:
        break
print(f"Liste sans Pastrami {sandwich_orders}")

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)
print(f"Liste final {finished_sandwiches}")