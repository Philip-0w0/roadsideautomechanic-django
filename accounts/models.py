from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    year = models.PositiveIntegerField()
    registration = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class ServiceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='service_records')
    booking = models.ForeignKey('bookings.BookingRequest', on_delete=models.SET_NULL, null=True, blank=True)
    service_date = models.DateField()
    description = models.TextField()
    odometer_km = models.PositiveIntegerField(null=True, blank=True)
    cost_cents = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle} — {self.service_date}"

    @property
    def cost_display(self):
        if self.cost_cents is None:
            return None
        return f"${self.cost_cents / 100:.2f}"