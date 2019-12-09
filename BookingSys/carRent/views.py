from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView


def index(request):
	Olist = CitiesOfCars.objects.order_by('city_name')
	return render(request, 'carRent/homePage1.html', {'object_list': Olist})
	
def city(request, city_id):
	cars = CarMod.objects.filter(city_name=CitiesOfCars.objects.get(pk=city_id))
	return render(request, 'carRent/carList.html', {'cars': cars})

def rent(request, car_id):
	car = CarMod.objects.get(pk=car_id)
	return render(request, 'carRent/index.html', {'car': car})

def payment(request):
	return render(request, 'carRent/payment.html')