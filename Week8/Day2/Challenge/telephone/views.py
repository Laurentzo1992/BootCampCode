from django.shortcuts import render
from django.http import request
from telephone.models import Personne

#Fonction to display all personnes
def personne(request):
	personnes = Personne.objects.all()
	return render(request, "telephone/personne.html", {"personnes":personnes})

#Fonction to display a personne at phone number
def personne_telephone(request, phone):
	personne = Personne.objects.get(phone=phone)
	return render(request, 'telephone/persone_tel.html', {"personne":personne})
	
#Fonction to display a personne at name
def personne_nom(request, nom):
	personne = Personne.objects.get(nom=nom)
	return render(request, "telephone/personne_nom.html", {"personne":personne})
# Create your views here.
