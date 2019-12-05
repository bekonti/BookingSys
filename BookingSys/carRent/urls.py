from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView # list of Data from DB
from carRent.models import *
from . import views

urlpatterns = [
	url(r'^$',	views.index),

	url('cities/<int:city_id>/', views.city),
]