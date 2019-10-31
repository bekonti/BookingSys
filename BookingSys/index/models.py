from django.db import models
# после  создание  модели 
# делаем миграцию (python manage.py makemigration after python manage.py migrate)
# чтобы добавить  в БД

class City(models.Model):
	city_name = models.CharField(max_length = 50)
	city_location = models.CharField(max_length = 50)

	def __str__(self):
		return self.city_name
	

class Hotel(models.Model):
	hotel_name = models.CharField(max_length = 50)		# имя отеля
	hotel_info = models.TextField()						# информация об отеле
	hotel_capacity = models.CharField(max_length = 10)  #сколько людей поместиться в отеле 
	hotel_stars = models.IntegerField()					#сколько  звёзд  у  отеля
	hotel_location = models.ForeignKey(City, on_delete = models.CASCADE) #в каждом городе есть отель

	def __str__(self):
		return self.hotel_name

