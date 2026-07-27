from django.contrib import admin
from .models import BookingRequest, AvailabilitySlot

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'vehicle_make', 'vehicle_model', 'service_category', 'status', 'created_at')
    list_filter = ('status', 'service_category')
    search_fields = ('customer_name', 'email', 'phone')

@admin.register(AvailabilitySlot)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', 'max_bookings', 'is_blocked')
    list_filter = ('date', 'is_blocked')