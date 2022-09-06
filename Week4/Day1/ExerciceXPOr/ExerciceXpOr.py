#Exercice 1 : Hello World-J'aime Python
print("Hello wolrd \n"*4,"I love python \n"*4)

#Exercice 2 : Quelle Est La Saison ?
mois = int(input("Veillez saisir le numero du mois : "))
if mois in range(3,6):
    print("Le printemps s'étend de mars (3) à mai (5)")
elif mois in range(6, 9):
    print("L'été s'étend du (6) juin au (8) août")
elif mois in range(9, 12):
    print("L'automne s'étend de septembre (9) à novembre (11)")
elif mois in range(0,2):
    print("L'hiver s'étend de décembre (12) à février (2)")
else:
    print("aucun temps disponible"