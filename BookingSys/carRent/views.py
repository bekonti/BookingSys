from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView


def index(request):
	object_list = CitiesOfCars.objects.order_by('city_name')
	return render(request, 'carRent/homePage1.html', {'object_list': object_list})
	
def city(request, city_id):
	cars = CarMod.objects.filter(city_name=CitiesOfCars.objects.get(pk=city_id))
	return render(request, 'carRent/carList.html', {'carses': cars})