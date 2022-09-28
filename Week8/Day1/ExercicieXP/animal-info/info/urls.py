from django.urls import path
from . import views

urlpatterns = [
    path('', views.family, name="family"),
    path('animal', views.animal, name="animal"),
]