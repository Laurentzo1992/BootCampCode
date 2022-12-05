#Exercice1

def get_words_from_file():
    with open('sowpods.txt', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
        print(text)
get_words_from_file()


import random
from random import randint
def get_random_sentence(length):
    phrase = []
    for i in range(length):
        phrase = phrase.append(get_words_from_file().random.randint(0,len(mots)))
        return phrase.join(" ")
get_random_sentence(6)


def main():
    print("\n Dans mon programme vous génèrez une phrase\n"
          "en specifiant sa taille le programme vous le contitue.\n")
    length = int(input('Saisir la taille (2 à 20) : '))
    if length >= 2 and length <= 20:
        print(get_random_sentence(length))
    else:
        print('incorrectes')

main()

#Exercice 2

import json
sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}

sampleJson["company"]["employee"]["payable"]["salary"]
sampleJson["company"]["employee"]["birth_date"] = "10/10/2021"
sampleJson
json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj)

json_file