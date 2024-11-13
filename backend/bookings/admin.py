from django.contrib import admin
from .models import FlightBooking,CarRental,HotelBooking

# Register your models here.
admin.site.register(FlightBooking)
admin.site.register(CarRental)
admin.site.register(HotelBooking)

