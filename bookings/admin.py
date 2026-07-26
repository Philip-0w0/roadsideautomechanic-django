from django.contrib import admin
from .models import BookingRequest

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'vehicle_make', 'vehicle_model', 'service_category', 'status', 'created_at')
    list_filter = ('status', 'service_category')
    search_fields = ('customer_name', 'email', 'phone')