from django.db import models
# Create your models here.

class Logistics_user(models.Model):
	contact_num = models.BigIntegerField(default=0, primary_key=True)
	email_id = models.CharField(max_length=80)
	name = models.CharField(max_length=90)
	password = models.CharField(max_length=30)

	def __unicode__(self):
		return str(self.contact_num)

class Orders(models.Model):
	order_id = models.IntegerField(default=0, primary_key = True)
	name = models.CharField(max_length=90, default=' ')
	goods_type = models.CharField(max_length=30)
	order_status = models.CharField(max_length=10)
	quantity = models.IntegerField(default=0)
	source = models.CharField(max_length=360)
	destination = models.CharField(max_length=360)
	add_contact_num = models.BigIntegerField(default=0)
	additional_info = models.CharField(max_length=360, default=' ')
	contact_num = models.ForeignKey(Logistics_user, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return str(self.order_id)


class Driver(models.Model):
	driver_id = models.IntegerField(default=0, primary_key=True)
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=20)

	def __unicode__(self):
	    return str(self.driver_id)

class Truck(models.Model):
    truck_id = models.IntegerField(default=0, primary_key = True)
    truck_number = models.CharField(max_length=20, default=' ')
    truck_capacity = models.IntegerField(default=0)
    truck_status = models.CharField(max_length=20, default='InGarage')
    driver_id = models.ForeignKey(Driver,null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.truck_id)

class Trip(models.Model):
	trip_id = models.IntegerField(default=0, primary_key=True)
	trip_capacity = models.IntegerField(default=0)
	location = models.CharField(max_length=360)
	status = models.CharField(max_length=20, default='InTransit')
	order_id = models.ForeignKey(Orders, null=True, on_delete=models.SET_NULL)
	truck_id = models.ForeignKey(Truck, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return str(self.trip_id)