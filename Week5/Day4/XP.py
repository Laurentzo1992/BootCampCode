#Exercice1

def get_words_from_file():
    with open('sowpods.txt', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
        print(text)
get_words_from_file()






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