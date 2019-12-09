from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView # list of Data from DB
from carRent.models import *
from . import views

app_name = 'CarRent'

urlpatterns = [
	url(r'^$',	views.index, name="index"),
   
	path(r'^/<int:city_id>/cities', views.city, name="cars"),
	path(r'^/<int:car_id>/cars', views.rent, name="rent"),
	path(r'^/payment', views.payment, name="payment"),
]