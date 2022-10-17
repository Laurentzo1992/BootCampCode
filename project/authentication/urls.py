from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('login_user', views.login_user, name="login_user"),
    path('logout_user', views.Logout_user, name='logout_user'),
     path('profile', views.profile, name='profile'),
    path('home', views.home, name='home'),
    path('add', views.add, name="add"),
    path('edit', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('users', views.users, name="users"),
    
]
