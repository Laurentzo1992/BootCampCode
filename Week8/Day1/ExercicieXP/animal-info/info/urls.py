from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal, name="animal"),
    path('family', views.family, name="family"),
]