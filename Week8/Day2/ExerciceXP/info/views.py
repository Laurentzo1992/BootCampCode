from django.shortcuts import render
from info.models import Animal, Famille 

def animaux(request):
	return render(request, "info/animaux.html", {})


def family(request):
	return render(request, "info/family.html", {})


def animal(request):
	return render(request, "info/animal.html", {})
# Create your views here.
