# Écrivez un programme qui accepte une séquence de mots séparés
# par des virgules en entrée et imprime les mots dans une séquence 
# séparée par des virgules après les avoir triés par ordre alphabétique.
# Utiliser la compréhension de liste

mots = input('saisir lea mot separe par des virgules : ')
mots = mots.split(',')
sequences = sorted(mots)
print(sequences)