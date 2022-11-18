from django.shortcuts import render, redirect
from django.http import request
from telephone.models import Personne
from .forms import PersonneForm
from django.contrib import messages

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

def add(request):
    if request.method=="POST":
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Telephone added successfully !")
            return redirect('personne')
        else:
            return render(request, 'telephone/add.html', {"form":form})
    else:
        form = PersonneForm()
        return render(request, 'telephone/add.html', {"form":form})
    
