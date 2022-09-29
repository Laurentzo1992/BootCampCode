from django.urls import path
from . import views

urlpatterns = [
	path('', views.people, name="people"),
  	path('people/<int:id>/', views.people_one, name="people_one"),
]
