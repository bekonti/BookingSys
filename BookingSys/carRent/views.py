from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView


def index(request):
	cities = CitiesOfCars.objects.order_by('city_name')
	return render(request, 'carRent/homePage1.html', {'cities': cities})
