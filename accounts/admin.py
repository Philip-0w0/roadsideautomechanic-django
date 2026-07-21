from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'make', 'model', 'year', 'registration', 'created_at')
    list_filter = ('make',)
    search_fields = ('make', 'model', 'registration', 'owner__username')