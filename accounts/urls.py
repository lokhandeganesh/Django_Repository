from django.urls import path

# From all modules import views#
from . import views

# set url patern for home/index page#
urlpatterns = [
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("logout",views.logout,name='logout'),
    
]