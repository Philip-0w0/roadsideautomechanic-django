from django.db import models
from django.contrib.auth.models import User
from accounts.models import Vehicle

class AvailabilitySlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_bookings = models.PositiveIntegerField(default=1)
    is_blocked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('date', 'start_time')
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.date} {self.start_time}"


class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    vehicle_make = models.CharField(max_length=60, blank=True)
    vehicle_model = models.CharField(max_length=60, blank=True)
    vehicle_year = models.PositiveIntegerField(null=True, blank=True)
    registration = models.CharField(max_length=20, blank=True)
    service_category = models.CharField(max_length=100)
    preferred_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    slot = models.ForeignKey(AvailabilitySlot, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} — {self.vehicle_make} {self.vehicle_model}"
