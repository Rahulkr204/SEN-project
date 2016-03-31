from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Orders, User, Trip, Driver, Truck


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'name')

class OrdersSerializer(serializers.ModelSerializer):
	user_id = UserSerializer()

	class Meta:
		model = Orders
		fields = ('order_id', 'user_id', 'goods_type', 'order_status', 'trip_id', 'quantity', 'source', 'destination', 'date', 'contact_num')

class TruckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Truck
        fields = ('truck_id', 'truck_capacity', 'remaining_capacity')

class TripSerializer(serializers.HyperlinkedModelSerializer):
	user_id = UserSerializer()
	order_id = OrdersSerializer()
	truck_id = TruckSerializer()

	class Meta:
		model = Trip
		fields = ('trip_id', 'trip_capacity', 'waypoint', 'location', 'user_id', 'order_id', 'truck_id')

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver_id', 'name', 'password')




