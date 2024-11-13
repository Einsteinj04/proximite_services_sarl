from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FlightBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flight_bookings')
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField(blank=True, null=True),
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Flight to {self.destination} on {self.departure_date}"
    
class CarRental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='car_rentals')
    car_type = models.CharField(max_length=100)
    rental_date = models.DateField()
    return_date = models.DateField()
    pickup_location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.user.username} - Car rental on {self.rental_date}"
    
class HotelBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotel_bookings')
    hotel_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Hotel {self.hotel_name} from {self.check_in_date} to {self.check_out_date}"