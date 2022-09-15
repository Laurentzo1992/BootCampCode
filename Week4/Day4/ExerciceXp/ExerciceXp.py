# Exercice 1

# Écrivez une fonction appelée display_message()qui imprime une phrase indiquant à tout le monde ce que vous apprenez dans ce cours.
# Appelez la fonction et assurez-vous que le message s'affiche correctement.

def display_message():
  print("Nous somme en apprentissage du bootcamp fullstack python django/Flask")
display_message()

# Exercice 2

# Écrivez une fonction appelée favorite_book()qui accepte un paramètre appelé title.
# La fonction doit imprimer un message, tel que "One of my favorite books is <title>".
# Par exemple : « L'un de mes livres préférés est Alice au pays des merveilles »
# Appelez la fonction, assurez-vous d'inclure un titre de livre comme argument lors de l'appel de la fonction.

def favorite_book(title):
  message = print(f"One of my favorite books is {title}")
  return message
favorite_book("Le respect des morts")

# Exercice 3

# Écrivez une fonction appelée describe_city()qui accepte le nom d'une ville et son pays comme paramètres.
# La fonction doit imprimer une phrase simple, telle que "<city> is in <country>".
# Par exemple "Reykjavik est en Islande"
# Donnez au paramètre de pays une valeur par défaut.
# Appelez votre fonction

def describe_city(ville, pays="Burkina Faso"):
  print(f"{ville} is in {pays}")
describe_city("Ouagadougou")

# Exercice 4

# Créez une fonction qui accepte un nombre entre 1 et 100 et génère un autre nombre aléatoirement entre 1 et 100.
# Comparez les deux nombres, si c'est le même nombre, affichez un message de réussite, sinon affichez un message d'échec et affichez les deux nombres.

import random
from random import randint
def randomNumber(a):
  randomNumb = random.randint(1, 100)
  if a== randomNumb:
    print("Succes!!!")
    print(f"The user number is {a} and the random number is {randomNumb}")
  else:
    print("failure...")
    print(f"The user number is {a} and the random number is {randomNumb}")
randomNumber(99)

# Exercice 5

