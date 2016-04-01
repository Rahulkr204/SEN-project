from django.db import models
from django.contrib.auth.models import User
#from .titles import mapping
from time import time
from django.forms import ModelForm

# Create your models here.
class Orders(models.Model):
	order_id = models.IntegerField(default=0, primary_key = True)
	user_id = models.ForeignKey(User)
	goods_type = models.CharField(max_length=30)
	order_status = models.CharField(max_length=10)
	trip_id = models.CharField(max_length=10)
	quantity = models.IntegerField(default=0)
	source = models.CharField(max_length=360)#check this once!
	destination = models.CharField(max_length=360)
	date = models.DateTimeField(db_index=True, auto_now_add=True)
	contact_num = models.CharField(max_length=30)#review once

class User(models.Model):
	user_id = models.CharField(max_length=100, primary_key=True)
	name = models.CharField(max_length=50)

class Truck(models.Model):
	truck_id = models.CharField(max_length=20, primary_key=True)
	truck_capacity = models.IntegerField(default=0)
	remaining_capacity = models.CharField(max_length=10)

class Trip(models.Model):
	trip_id = models.CharField(max_length=20, primary_key=True)
	trip_capacity = models.CharField(max_length=20)
	waypoint = models.CharField(max_length=360)#check this once!
	location = models.CharField(max_length=360)
	user_id = models.ForeignKey(User)
	order_id = models.ForeignKey(Orders)
	truck_id = models.ForeignKey(Truck)

class Driver(models.Model):
	driver_id = models.IntegerField(default=0, primary_key=True)
	name = models.CharField(max_length=30, default='x')
	password = models.CharField(max_length=20)
	#attendance = models.CharField(max_length=30)

