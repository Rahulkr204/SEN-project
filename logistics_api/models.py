from django.db import models
from time import time
from django.forms import ModelForm

# Create your models here.

class Logistics_user(models.Model):
	contact_num = models.IntegerField(default=0, primary_key=True)#check the range of this integer! Also make this a biginteger!
	email_id = models.CharField(max_length=80)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=30)

	def __str__(self):
		return str(self.contact_num)

class Orders(models.Model):
	order_id = models.IntegerField(default=0, primary_key = True)
	goods_type = models.CharField(max_length=30)
	order_status = models.CharField(max_length=10)
	quantity = models.IntegerField(default=0)
	source = models.CharField(max_length=360)
	destination = models.CharField(max_length=360)
	#date = models.DateTimeField(db_index=True, auto_now_add=True)#take in milliseconds as long. (Use BigInteger field in models)
	contact_num = models.ForeignKey(Logistics_user, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return str(self.order_id)

class Truck(models.Model):
	truck_id = models.CharField(max_length=20, primary_key=True)
	truck_capacity = models.IntegerField(default=0)
	remaining_capacity = models.CharField(max_length=10)#change this to integer field

	def __str__(self):
		return str(self.truck_id)

class Trip(models.Model):
	trip_id = models.CharField(max_length=20, primary_key=True)
	trip_capacity = models.CharField(max_length=20)#integer field
	waypoint = models.CharField(max_length=360)#check this once!check the maximum capacity of the cahracter field.
	location = models.CharField(max_length=360)
	order_id = models.ForeignKey(Orders, null=True, on_delete=models.SET_NULL)
	truck_id = models.ForeignKey(Truck)

	def __str__(self):
		return str(self.trip_id)

class Driver(models.Model):
	driver_id = models.IntegerField(default=0, primary_key=True)
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	trip_id = models.ForeignKey(Trip, null=True, on_delete=models.SET_NULL)
