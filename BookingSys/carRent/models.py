from django.db import models

class CitiesOfCars(models.Model):
	city_name = models.CharField(max_length = 50)
	city_location = models.CharField(max_length = 50)
	city_Img = models.ImageField(upload_to='cityImg/', default='NULL')

	def __str__(self):
		return self.city_name



class CarMod(models.Model):
	class Meta():
		db_table = "carModels"
	WHITE = 'white'
	BLACK = 'black'
	YELLOW = 'yellow'
	GRAY = 'gray'

	COLOUR_CHOICES = (
		(WHITE, 'White'),
		(BLACK, 'Black'),
		(YELLOW, 'Yellow'),
		(GRAY, 'Gray'),
	)
	
	car_name = models.CharField(max_length = 50)
	city_name = models.ForeignKey(CitiesOfCars, on_delete = models.CASCADE)
	frontImg = models.ImageField(upload_to='carImg/', default='NULL')
	janImg = models.ImageField(upload_to='carImg/', default='NULL')
	ishImg = models.ImageField(upload_to='carImg/', default='NULL')
	madeDate = models.IntegerField(default=2000)
	amount = models.IntegerField(default=20)
	car_colour = models.CharField(max_length = 50, choices = COLOUR_CHOICES, default = WHITE)
	def __str__(self):
		return self.car_name
	
	
# Create your models here.
