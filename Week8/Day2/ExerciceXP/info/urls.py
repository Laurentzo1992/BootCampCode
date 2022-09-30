
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.animaux, name="animaux"),
    path('family/<int:id>/', views.family, name="family"),
    path('animal/<int:id>/', views.animal, name="animal"),
    

    
]
