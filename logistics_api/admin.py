from django.contrib import admin
from .models import Logistics_user, Orders, Trip, Truck, Driver
# Register your models here.

admin.site.register(Logistics_user)
admin.site.register(Orders)
admin.site.register(Trip)
admin.site.register(Truck)
admin.site.register(Driver)