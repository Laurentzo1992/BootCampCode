#Date de naissance au format day/mois/année
Naissance=input("Date d'anniverssaire?\nDonner en jour/ mois/ année:exemple:05/10/2000==>")
t=""
Naissance.split(',')
i=Naissance[-1]
annee=Naissance[6:10]
annee=int(annee)
print(annee)
if(annee%4==0 and annee%100!= 0 or annee%400==0):
    for x in range(2):
        for i in range(0,int(i)):
            t +="i"
        print("    __",t,"__")
        print("   |:H:a:p:p:y:|")
        print(" __|___________|__")
        print("|^^^^^^^^^^^^^^^^^^|")
        print("| :B:i:r:t:h:d:a:y:|")
        print("|                  |")
        print("~~~~~~~~~~~~~~~~~~~~")
else:
    for i in range(0,int(i)):
        t +="i"
    print("    __",t,"__")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^^|")
    print("| :B:i:r:t:h:d:a:y:|")
    print("|                  |")
    print("~~~~~~~~~~~~~~~~~~~~")