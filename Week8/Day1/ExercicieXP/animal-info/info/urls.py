from django.urls import include, path
from . import views

urlpatterns = [
    path('family/<int:id>/', views.family),
    path('animal/<int:id>/', views.animal),
]