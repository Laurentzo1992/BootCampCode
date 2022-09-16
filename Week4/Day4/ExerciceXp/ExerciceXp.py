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

# Écrivez une fonction appelée make_shirt()qui accepte une taille et le texte d'un message qui doit être imprimé sur la chemise.
# La fonction doit imprimer une phrase résumant la taille de la chemise et le message imprimé dessus, comme"The size of the shirt is <size> and the text is <text>"
# Appelez la fonction make_shirt().

# Modifiez la make_shirt()fonction pour que les chemises soient grandes par défaut avec un message indiquant "J'aime Python" par défaut.
# Faire une grande chemise avec le message par défaut
# Faire une chemise moyenne avec le message par défaut
# Faites une chemise de n'importe quelle taille avec un message différent.

# Bonus : Appelez la fonction make_shirt()en utilisant des arguments mot-clé.

def make_shirt(size=100, text="J'aime Python"):
  print(f"The size of the shirt is {size} and the text is {text}")
make_shirt()

# Exercice 6

# En utilisant cette liste de noms de magiciens. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Passez la liste à une fonction appelée show_magicians(), qui imprime le nom de chaque magicien de la liste.
# Écrivez une fonction appelée make_great()qui modifie la liste des magiciens en ajoutant la phrase "the Great"au nom de chaque magicien.
# Appelez la fonction make_great().
# Appelez la fonction show_magicians()pour voir que la liste a bien été modifiée.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for i in range(len(magician_names)):
        print(magician_names[i])

def make_great():
    for i in magician_names:
        i = i + " the Great"
        print(i)
make_great()

# Exercice 7


# Créez une fonction appelée get_random_temp().
# Cette fonction doit renvoyer un entier entre -10 et 40 degrés (Celsius), sélectionné au hasard.
# Testez votre fonction pour vous assurer qu'elle génère les résultats attendus.

# Créez une fonction appelée main().
# Dans cette fonction, appelez get_random_temp()pour obtenir une température et stockez sa valeur dans une variable.
# Informez l'utilisateur de la température dans un message amical, par ex. "La température actuelle est de 32 degrés Celsius."

# Ajoutons plus de fonctionnalités à la main()fonction. Écrivez quelques conseils amicaux concernant la température :
# en dessous de zéro (par exemple "Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
# entre zéro et 16 (ex. "Assez froid ! N'oubliez pas votre manteau")
# entre 16 et 23
# entre 24 et 32
# entre 32 et 40

# Modifiez la get_random_temp()fonction :
# Ajoutez un paramètre à la fonction, nommé 'saison'.
# À l'intérieur de la fonction, au lieu de simplement générer un nombre aléatoire entre -10 et 40, définissez des limites inférieures et supérieures en fonction de la saison, par exemple. si la saison est 'hiver', les températures ne devraient tomber qu'entre -10 et 16.
# Maintenant que nous avons changé get_random_temp(), changeons la main()fonction :
# Avant d'appeler get_random_temp(), nous devrons décider d'une saison, afin que nous puissions appeler la fonction correctement. Demandez à l'utilisateur de saisir une saison : "été", "automne" (vous pouvez utiliser "automne" si vous préférez), "hiver" ou "printemps".
# Utilisez la saison comme argument lors de l'appel get_random_temp().

# Bonus : Donnez la température sous forme de nombre à virgule flottante au lieu d'un entier.
# Bonus : Au lieu de demander la saison, demandez à l'utilisateur le numéro du mois (1 = janvier, 12 = décembre). Déterminez la saison en fonction du mois.

import random
from random import randint

#Créez une fonction appelée get_random_temp()

def get_random_temp():
    tmpvalue = random.randint(-10, 40)
    return tmpvalue

# Creér une fonction main
def main():
# Appelze la fonction get_random_temp() et satocker la valeur dans une variable

    randtmp = get_random_temp()
    print(f"la temperature actuelle est de {randtmp} dégré celsus")
    if randtmp < 0:
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif randtmp >0 and randtmp < 16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif randtmp >=16 and randtmp <= 23:
        print("Un peut frais cas même mais beau temps")
    elif randtmp >=24 and randtmp < 32:
        print("Tres beau temps")
    elif randtmp >=32 and randtmp < 40:
        print("Quel challeur ! il fau la clim!!!")
    else:
        print("Mauvais temps trop de chaleur")
main()

