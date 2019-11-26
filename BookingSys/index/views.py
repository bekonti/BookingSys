from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView
from .forms import *


def index(request):
	best_hotels = Hotel.objects.order_by('-hotel_capacity')
	return render(request, 'index/homepage.html', {'hotels': best_hotels})


def hotel(request, hotel_id):
	hotel = get_object_or_404(Hotel, pk = hotel_id)
	hotels_fb = showFeedbacks(request, hotel_id)

	if request.method == 'POST':
		try:
			txt = request.POST.get("fb_text")
			print(request.POST)
			feedBack = FeedBack(fb_text = txt, hotel = Hotel.objects.get(pk=hotel_id),
								user = SimpleUser.objects.get(username=request.POST["username"]))
			feedBack.save()
		except:
			print("The Feed-Backs cannot be added")
	return render(request, "index/hotel.html", {"hotel":hotel,
												"feedBacks":hotels_fb})

def showFeedbacks(request, hotel_id):
    try:
        feedBacks = FeedBack.objects.filter(hotel=Hotel.objects.get(pk=hotel_id))
        return feedBacks
    except:
        return "No FeedBacks yet"

def addFeedback(request, hotel_id):
	try:
		txt = request.POST.get("feedBacks_text")
		feedBack = FeedBack(fb_text = txt, 
							hotel = Hotel.objects.get(pk=hotel_id))
		feedBack.save()
		return render(request, "index.hotel.html", {"hotel":Hotel.objects.get(pk=hotel_id)})
	except:
		return HttpResponse("No such Hotel (")

class registerView(CreateView):
	form_class = SimpleUserForm
	success_url = reverse_lazy('login')
	template_name = 'registration/register.html'


def profile(request):
	return render(request, "index/userPage.html")