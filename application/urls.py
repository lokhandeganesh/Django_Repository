from django.urls import path

# From all modules import views#
from . import views

# set url patern for home/index page#
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
]