from django.shortcuts import render
from info.models import Animal, Famille 

def animaux(request):
	animaux = Animal.objects.all()
	return render(request, "info/animaux.html", {"animaux":animaux})


def family(request, id):
	animaux = Animal.objects.filter(famille=id)
	return render(request, "info/family.html", {"animaux":animaux})


def animal(request, id):
	animal = Animal.objects.get(id=id)
	return render(request, "info/animal.html", {"animal":animal})
# Create your views here.
