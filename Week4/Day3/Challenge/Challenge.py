#Defi 1


#Demander un mot à un utilisateur
# Écrivez un programme qui crée un dictionnaire. Ce dictionnaire stocke les index de chaque lettre dans une liste.

# Assurez-vous que les lettres sont les clés.
# Assurez-vous que les lettres sont des chaînes.
# Assurez-vous que les index sont stockés dans une liste et que ces listes sont des valeurs.

mot = input("Veillez saisir un mot : ")
mot = {lettre: [mot.index(lettre) for i in lettre] for lettre in mot}
print(mot)



#Defi 2