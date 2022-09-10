#Exercice 1

#Écrivez un programme qui calcule et imprime une valeur selon cette formule donnée :
#Q = Square root of [(2 * C * D)/H]
#oici les valeurs fixes de C et H :
#C est 50.
#H a 30 ans.
#Demandez à l'utilisateur une chaîne de nombres séparés par des virgules, utilisez chaque nombre de l'utilisateur comme Ddans la formule et renvoyez tous les résultats
#Par exemple, si l'utilisateur saisit : 100,150,180
#La sortie doit être :

import math
C = 50
H = 30
s = input("Veillez saisir des nombre seprer par des virgules : ")
Listes = s.split(",")
print(Listes)
for i in Listes:
    Q = math.sqrt(((2*C*int(i))/H))
    print(Q, end=",")



#Exercice 2

Liste = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
for i in Liste:
    listeNombre = i
    print(i, end=" ")




#Exercice 3


text = "L’expression « poésie scientifique » fut forgée en France par le poète René Ghil par contraste avec la poésie symboliste de Mallarmé (De la poésie scientifique, 1909)1 et fut reprise, dans un contexte plus large, par Casimir Fusil dans La poésie scientifique de 1750 à nos jours (1918)2, où nous trouvons la définition suivante : « La poésie scientifique, en tant que poésie, s’attache aux idées générales de la science, capables d’émotion, plus encore qu’aux faits eux-mêmes […] Pour nous la poésie scientifique est donc celle qui fait directement sortir l’émotion des découvertes de la science et de ses chiffres, ou qui se meut dans la zone où la philosophie voisine avec la science »3. À son origine, cette expression était donc appliquée à la poésie contemporaine, ce qui pourrait fonder la réflexion sur le possible anachronisme de la démarche d’Albert-Marie Schmidt qui, dans La Poésie scientifique au XVIe siècle (1938)4 adopta le syntagme pour désigner un ensemble des poèmes de la Renaissance visant à véhiculer un savoir sur la Nature."
print(f"le text contient {len(text)} caracteres ")
print("le text contien ", len(text.split(".")), "phrases")
print("Le texte conient : ", len(text.split()), "mots")
print("Le texte conient : ", len(set(text.split())), "mots uniques")
print(len("".join(text)))



#Exercice 4

#Écrivez un programme qui calcule et imprime une valeur selon cette formule donnée :

chaine = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
#for lette in chaine:
  #  print(f"{lette} : {chaine.count(lette)}")

l = [(x, chaine.count(x)) for x in set(chaine)]
print(l)