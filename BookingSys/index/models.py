from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings
# # после  создание  модели 
# # делаем миграцию (python manage.py makemigration after python manage.py migrate)
# # чтобы добавить  в БД

class City(models.Model):
	city_name = models.CharField(max_length = 50)
	city_location = models.CharField(max_length = 50)

	def __str__(self):
		return self.city_name
	

class Hotel(models.Model):
	hotel_name = models.CharField('name of Hotel', max_length = 50)		# имя отеля
	hotel_info = models.TextField('Info about Hotel',)						# информация об отеле
	hotel_capacity = models.IntegerField(default = 0)  			#сколько людей поместиться в отеле 
	hotel_stars = models.IntegerField(default = 0)					#сколько  звёзд  у  отеля
	hotel_location = models.ForeignKey(City, on_delete = models.CASCADE) #в каждом городе есть отель

	def __init__(self):
		self.lux = int(self.hotel_capacity * 0.2)
		self.eco = self.hotel_capacity - self.lux

	def __str__(self):
		return self.hotel_name + ' ' + str(self.lux) + ' ' + str(self.eco)


class FeedBack(models.Model):
	fb_text = models.TextField('text of feedback to Hotel')
	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	fb_date = models.DateTimeField('data published')


class SimpleUser(AbstractUser):
	userImg = models.ImageField(upload_to='user_avas/', default='NULL')

	def __str__(self):
		return self.username
	# def __init__(self, arg):
	# 	super(FeedBack, self).__init__()
	# 	self.arg = arg
	
# # class Room(models.Model):
# # 	hotel_room = models.ForeignKey(Hotel, on_delete = models.CASCADE) # к какому отелю  принадлежит комната
# # 	# room_id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = "ID")
# # 	rooms = models.IntegerField() 					# количество комнат
# # 	roomType = models.CharField(max_length = 20) 	# тип номера (эконом, люкс)


# # 	def __init__(self, arg):
# # 		pass	

# # 	def __str__(self):
# # 		return self.room_id
				
# # class Booking(models.Model):
# 	# hotel_id =
	
