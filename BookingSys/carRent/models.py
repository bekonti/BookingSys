from django.db import models
import datetime
from django.utils import timezone



class Payment(models.Model):
	name = models.CharField(max_length = 50)
	surname = models.CharField(max_length = 50)
	tel = models.CharField(max_length = 11)
	email = models.EmailField(max_length = 50)
	start_rent = models.DateTimeField('starting date',null=True, blank=True)
	end_rent = models.DateTimeField('ending date',null=True, blank=True)
	
	def __str__(self):
		return self.name

class CitiesOfCars(models.Model):
	city_name = models.CharField(max_length = 50)
	city_location = models.CharField(max_length = 50)
	city_Img = models.ImageField(upload_to='cityImg/', default='NULL')

	def __str__(self):
		return self.city_name



class CarMod(models.Model):
	class Meta():
		db_table = "carModels"
	
	car_name = models.CharField(max_length = 50)
	city_name = models.ForeignKey(CitiesOfCars, on_delete = models.CASCADE)
	frontImg = models.ImageField(upload_to='carImg/', default='NULL')
	janImg = models.ImageField(upload_to='carImg/', default='NULL')
	ishImg = models.ImageField(upload_to='carImg/', default='NULL')
	madeDate = models.IntegerField(default=2000)
	amount = models.IntegerField(default=20)
	def __str__(self):
		return self.car_name
	

