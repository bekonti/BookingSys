from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView
from .forms import *


def index(request):
	best_hotels = Hotel.objects.order_by('hotel_capacity')
	return render(request, 'index/homePage.html', {'hotels': best_hotels})


def hotel(request, hotel_id):
	hot = get_object_or_404(Hotel, pk = hotel_id)


def showFeedbacks(request, hotel_id):
    try:
        feedBacks = Comments.objects.filter(article=Article.objects.get(pk=article_id))
        return comments
    except:
        return "No comments yet"


class registerView(CreateView):
	form_class = SimpleUserForm
	success_url = reverse_lazy('login')
	template_name = 'registration/register.html'