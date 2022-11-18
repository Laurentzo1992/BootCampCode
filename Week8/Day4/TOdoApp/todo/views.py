from django.shortcuts import render
from todo.models import Category, Todo


def home(request):
    cats = Category.objects.order_by('name')
    context = {"cats":cats}
    return render(request, 'todo/home.html', context)

# Create your views here.
