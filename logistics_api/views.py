from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from serializers import UserSerializer, OrdersSerializer, TruckSerializer, TripSerializer, DriverSerializer
from models import Orders, Logistics_user, Truck, Trip, Driver
from django.http import HttpResponse
from rest_framework.response import Response



class OrdersList(APIView):

    def get(self, request, format=None):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        queryset = Orders.objects.all()
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverList(APIView):
    #permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        queryset = Driver.objects.all()
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TripList(APIView):

    def get(self, request, format=None):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        queryset = Trip.objects.all()
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TruckList(APIView):

    def get(self, request, format=None):
        trucks = Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        queryset = Truck.objects.all()
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):

    def get(self, request, format=None):
        users = Logistics_user.objects.all()
        serializer = UserSerializer(users, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        queryset = Logistics_user.objects.all()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get(self, request, pk, format=None):
        user = Logistics_user.objects.filter(pk=pk)
        serializer = UserSerializer(user , many=True, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = Logistics_user.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)#, many=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = Logistics_user.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrdersDetail(APIView):

    def get(self, request, pk):
        order = Orders.objects.filter(pk=pk)
        serializer = OrdersSerializer(order , many=True, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        order = Orders.objects.get(pk=pk)
        serializer = OrdersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = Orders.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TruckDetail(APIView):

    def get(self, request, pk):
        truck = Truck.objects.filter(pk=pk)
        serializer = TruckSerializer(truck , many=True, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        truck = Truck.objects.get(pk=pk)
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        truck = Truck.objects.get(pk=pk)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TripDetail(APIView):

    def get(self, request, pk):
        trip = Trip.objects.filter(pk=pk)
        serializer = TripSerializer(trip , many=True, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DriverDetail(APIView):

    def get(self, request, pk):
        driver = Driver.objects.filter(pk=pk)
        serializer = DriverSerializer(driver , many=True, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        driver = Driver.objects.get(pk=pk)
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        driver = Driver.objects.get(pk=pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    return render(request, 'homepage.html')
