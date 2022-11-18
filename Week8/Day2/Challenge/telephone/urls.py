from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.personne, name="personne"),
    path("personne/<int:phone>/", views.personne_telephone, name="personne_telephone"),
    path("personne/<str:nom>/", views.personne_nom, name="personne_nom"),
    path("personne/add", views.add, name="add"),
]

