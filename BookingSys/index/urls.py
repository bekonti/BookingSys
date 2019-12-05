from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView # list of Data from DB
from index.models import *
from django.contrib.auth.views import auth_login
from . import views

app_name = 'Hotel'
urlpatterns = [
	#localhost:8000
	url(r'^$',	views.index, name = 'index'),
    #localhost:8000
	path('<int:city_id>/', views.byCity, name="HotelsByCity"),

    #login page
    path('', auth_login, name="login"),
	
	#localhost:8000/hotel/id
	path('hotel/<int:hotel_id>/', views.hotel, name='hotel'),
	
    #registraion
    path("register", views.registerView.as_view(), name="registration"),

    path("user/", views.profile, name='profile'),
    #add Feedback
    path('hotel/<int:hotel_id>/fb/', views.addFeedback, name='addFeedback')
]