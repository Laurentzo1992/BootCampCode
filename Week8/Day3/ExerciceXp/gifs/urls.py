
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_gif', views.add_gif, name='add_gif'),
    path('add_cat', views.add_cat, name='add_cat'),
    path('cat', views.cat, name='cat'),
]