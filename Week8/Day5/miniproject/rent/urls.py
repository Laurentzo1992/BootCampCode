from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rent/rental', views.rental, name='rental'),
    
]
  
 