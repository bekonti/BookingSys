from django.conf.urls import url, include
from django.views.generic import ListView, DetailView # list of Data from DB
from index.models import *
from . import views

urlpatterns = [
	url(r'^$',	views.flights, name = 'flights'),
	# url(r'^$',
		# ListView.as_view(queryset=Hotel.objects.all().order_by("id")[:10],
		# template_name = "index.HomePage.html")),
]