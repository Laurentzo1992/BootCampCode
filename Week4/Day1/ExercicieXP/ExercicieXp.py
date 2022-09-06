#Exercice 1
print("EXERCIE 1 \n")
print("Hello world \n"*4)
print("EXERCIE 2 \n")

#Exercicie 2
print((99^3)*8)

print("EXERCIE 3 \n")
#Exercicie 3
5<3
#true
3==3
# true
3=='3'
# false
"Hello"=="Hello"
# true

print("EXERCIE 4 \n")
#Exercicie 4
computer_brand = "HP PAVILLON"
print(f"I have a {computer_brand} computer")

print("EXERCIE 5 \n")
#Exercicie 5
name = "NIKIEMA Laurent"
age = 29
shoe_size = 42
info = f"je suis {name} agé de {age} et je chaussse {shoe_size}"
print(info)

print("EXERCIE 6 \n")
#Exercice 6

a,b = 15,12
if a>b:
    print("Hello world")
#Exercicie 7
print("EXERCIE 7 \n")

nombre = int(input("Veillez saisir un nombre : "))
if nombre%2==0:
    print(f"Le nombre{nombre} est paire")
else:
    print(f"{nombre} est impaire")

#Exercicie 8
print("EXERCIE 8 \n")
nomPropre = "Laurent"
nom = input("Veillez saisir votre nom :")
if nom == nomPropre:
    print(f"Super vous être vous même car vous appelez {nomPropre}")
else:
    print(f"Intruit dehors.......{nom}")

#Exercice 9
print("EXERCIE 9 \n")

#valeur constante de pouce
pouce = 2.54
taillePouce = float(input("Veillez saisir votre taille en pouce :")) #l'untilisateur entre sa taille en pouce
maTailleCentime = pouce*taillePouce # produit de la taille par la valeur constante de pouce pour avoir en cm
if maTailleCentime > 145: #condition si la taille en cm est superieur en 145cm
    print(f"votre atille est de {maTailleCentime} cm vous pouvez roulez") #affiche
else: # si non 
    print(f"Vous taille est de {maTailleCentime} cm allez jouer au basket pour grandir un peut") # affiche 





