from django.contrib.auth.models import User, Group
import requests
from rest_framework import serializers
from models import Orders, Logistics_user, Trip, Driver, Truck


class UserSerializer(serializers.HyperlinkedModelSerializer):
    context={'request': requests}
    class Meta:
        model = Logistics_user
        fields = ('contact_num', 'email_id','name', 'password')

class OrdersSerializer(serializers.ModelSerializer):
	context={'request': requests}
	#contact_num = UserSerializer()

	class Meta:
		model = Orders
		fields = ('order_id', 'goods_type', 'order_status', 'quantity', 'source', 'destination', 'contact_num')

class TruckSerializer(serializers.HyperlinkedModelSerializer):
    context={'request': requests}
    class Meta:
        model = Truck
        fields = ('truck_id', 'truck_capacity', 'remaining_capacity')

class TripSerializer(serializers.HyperlinkedModelSerializer):
	context={'request': requests}
	#order_id = OrdersSerializer()
	#truck_id = TruckSerializer()

	class Meta:
		model = Trip
		fields = ('trip_id', 'trip_capacity', 'waypoint', 'location', 'order_id', 'truck_id')

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    context={'request': requests}
    class Meta:
        model = Driver
        fields = ('driver_id', 'name', 'password', 'trip_id')




