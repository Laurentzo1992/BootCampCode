from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rent/rental', views.rental, name='rental'),
    path('rent/rental/<int:id>', views.rental_detail, name='rental_detail'),
    path('rent/rental/add', views.add_rent, name='add_rent'),
    
    path('rent/customer/add', views.add_cust, name='add_cust'),
    path('rent/customer', views.customer, name='customer'),
    path('rent/customer/<int:id>', views.customer_detail, name='customer_detail'),
    
    path('rent/vehicle/add', views.add_vehi, name='add_vehi'),
    path('rent/vehicle', views.vehicle, name='vehicle'),
    path('rent/vehicle/<int:id>', views.vehicle_detail, name='vehicle_detail'),
    
]
  
 