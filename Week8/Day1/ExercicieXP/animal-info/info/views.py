
from django.shortcuts import render
from django.http import HttpResponse, request, response





def family(request):
    
    datas = {
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 3,
            "name": "mammifère"
        },
        {
            "id": 4,
            "name": "reptile"
        },
        {
            "id": 5,
            "name": "insecte"
        },
        {
            "id": 6,
            "name": "arachnide"
        },
        {
            "id": 7,
            "name": "amphibie"
        },
        {
            "id": 8,
            "name": "vvipar"
        },
        {
            "id": 9,
            "name": "ovipar"
        }
    ]
    }
    return render(request, "info/family.html", {"datas":datas})

def animal(request):
    datas = {
    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2,
            "image ":"https://www.parcomega.ca/app/uploads/2022/05/header-famille-animaux-3-768x768.png"
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1,
            "image ":"https://www.parcomega.ca/app/uploads/2022/05/header-famille-animaux-3-768x768.png"
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1,
            "image ":"https://www.parcomega.ca/app/uploads/2022/05/header-famille-animaux-3-768x768.png"
        }
    ]
    }
    return render(request, "info/animal.html", {"datas":datas})
    
    
    

# Create your views here.
