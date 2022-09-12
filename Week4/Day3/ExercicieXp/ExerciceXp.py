#Exercice 1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# ZipList = dict(zip(keys, values))
# print(ZipList)

#Exercice 2

# valuepay = list()
# ageMoin3 = 0
# ageCompris12 = 10
# agePlusDe12 = 15
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# for value in family.values():
#     if value >= 0 and value <3:
#         print("Le ticket est gratuit :")
#         valuepay.append(ageMoin3)
#     elif value >= 3 and value <= 12:
#         print(f"Le ticket coute {ageCompris12}$")
#         valuepay.append(ageCompris12)
#     else:
#         print(f"Le ticket coute {agePlusDe12}$")
#         valuepay.append(agePlusDe12)
# print(f"La liste des couts par membre {valuepay}")
# print(f"Cout total pour la famile {sum(valuepay)}$")



#Exercicie 3

#Créez un dictionnaire appelé branddont la valeur correspond 
#aux informations de la première partie (transformez les informations 
#en clés et valeurs ).

brand = {"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":
{"France": "blue",
    "Spain": "red",
    "US": ["pink", "green"]
}
}
brand['number_stores'] = 2
# Imprimez une phrase qui explique qui sont les clients de Zaras.
print(f"les clients de zaras sont les : {brand['type_of_clothes']}")
# Ajoutez une clé appelée country_creationavec une valeur de Spain.
brand['country_creation'] = " Spain"
# Vérifiez si la clé international_competitorsest dans le dictionnaire. Si c'est le cas, ajoutez le magasin Desigual .
if brand['international_competitors']:
    brand['international_competitors'].append('Desigual')
# Supprimez les informations sur la date de création.
del brand['creation_date']

# Imprimez le dernier concurrent international.
print(brand['international_competitors'][-1])
# Imprimez les principales couleurs de vêtements aux États-Unis.
print(brand['major_color']['US'])
# Imprimez le nombre de paires clé-valeur (c'est-à-dire la longueur du dictionnaire).
print(f"La longueur du dictionnaire est : {len(brand)}")
# Imprimez les clés du dictionnaire.
print(brand.keys())

more_on_zara = {
"creation_date": 1975,
"number_stores": 10000
}
brand.update(more_on_zara)
print(f" La nouvelle valeur du nombre de magasin est : brand['number_stores']")
#print(brand)
#print(more_on_zara)




#Exercice 4

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# #Utilisez une boucle for pour recréer le 1er résultat. Astuce : ne codez pas les numéros en dur.
# disney_users_A = {users[i]: i for i in range(len(users))}
# print(disney_users_A)
# #Utilisez une boucle for pour recréer le 2ème résultat. Astuce : ne codez pas les numéros en dur.
# disney_users_B = {i: users[i] for i in range(len(users))}
# print(disney_users_B)
# #Utilisez une méthode pour recréer le 3ème résultat. Astuce : Le 3ème résultat #est trié par ordre alphabétique.
# disney_users = sorted(disney_users_A, reverse=False)
# disney_users_C = {disney_users[i]: i for i in range(len(disney_users))}
# print(disney_users_C)
# #Les caractères dont les noms contiennent la lettre "i".
# disney_users_D = {users[i]: i for i in range(len(users)) if "i" in users[i]}
# print(disney_users_D)
# #Les caractères, dont les noms commencent par la lettre « m » ou « p ».
# disney_users_E = {users[i]: i for i in range(len(users)) if users[i][2] == "m" or users[i][0] == "p"}
# print(disney_users_E)



