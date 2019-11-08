from django.db import models

class dep_city(models.Model):
	city_name = models.CharField(max_length = 50)
	city_location = models.CharField(max_length = 50)

	def __str__(self):
		return self.city_name

class arr_city(models.Model):
	city_name = models.CharField(max_length = 50)
	city_location = models.CharField(max_length = 50)

	def __str__(self):
		return self.city_name
	

class info_com(models.Model):
	com_name = models.CharField(max_length = 50)		# имя компании
	com_info = models.TextField()						# информация о компании обслуживающий перелет
	plane_capacity = models.CharField(max_length = 10)  #сколько людей поместиться в самолете 
	flight_price = models.IntegerField(max_length = 10)    # цена перелета
	check_for_bagg= models.booleanField()               #проверяем есть ли возможность перевезти багаж
	check_for_vip= models.booleanField()                #проверяем на VIP 
	
	

	def __str__(self):
		return self.com_name


