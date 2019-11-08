from django.shortcuts import render

def flights(request):
	return render(request, 'flights/homePage.html')
