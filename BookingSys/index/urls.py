from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView # list of Data from DB
from index.models import *
from . import views

app_name = 'Hotel'
urlpatterns = [
	#localhost:8000
	url(r'^$',	views.index, name = 'index'),
	#localhost:8000/hotel/id
	path('hotel/<int:hotel_id>/', views.hotel, name='hotel'),
	
    path("register", views.registerView.as_view(), name="registration"),
]