from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def rental(request):
    context ={}
    return render(request, 'rental.html', context)

# Create your views here.
