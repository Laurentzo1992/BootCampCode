from django.shortcuts import render, redirect
from urllib import request, response
from gifs.models import Gifs, Categorie
from .forms import GifForm, CategoryForm
from django.contrib import messages



def home(request):
    gifs = Gifs.objects.all()
    context = {"gifs":gifs}
    return render(request, "gifs/home.html", context)


def add_gif(request):
    if request.method=="POST":
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gifs ajouté avec successfully !")
            return redirect('home')
        else:
            return render(request, 'gifs/add_gif.html', {"form":form})
    else:
        form = GifForm()
        return render(request, 'gifs/add_gif.html', {"form":form})
    

def add_cat(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categorie ajouté avec successfully !")
            return redirect('cat')
        else:
            return render(request, 'gifs/add_gif.html', {"form":form})
    else:
        form = CategoryForm()
        return render(request, 'gifs/add_gif.html', {"form":form})
    

def cat(request):
    cats = Categorie.objects.all()
    context = {"cats":cats}
    return render(request, 'gifs/cat.html', context)

# Create your views here.
