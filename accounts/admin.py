from django.contrib import admin
from .models import Vehicle, ServiceRecord

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'make', 'model', 'year', 'registration', 'created_at')
    list_filter = ('make',)
    search_fields = ('make', 'model', 'registration', 'owner__username')

@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service_date', 'odometer_km', 'cost_display', 'created_at')
    list_filter = ('service_date',)
    search_fields = ('vehicle__make', 'vehicle__model', 'description')