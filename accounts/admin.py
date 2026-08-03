from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Vehicle, ServiceRecord


class VehicleInline(admin.TabularInline):
    model = Vehicle
    extra = 0
    fields = ('make', 'model', 'year', 'registration')


class CustomUserAdmin(UserAdmin):
    inlines = [VehicleInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class ServiceRecordInline(admin.TabularInline):
    model = ServiceRecord
    extra = 0
    fields = ('service_date', 'description', 'cost_cents')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'make', 'model', 'year', 'registration', 'created_at')
    list_filter = ('make',)
    search_fields = ('make', 'model', 'registration', 'owner__username')
    inlines = [ServiceRecordInline]


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service_date', 'odometer_km', 'cost_display', 'created_at')
    list_filter = ('service_date',)
    search_fields = ('vehicle__make', 'vehicle__model', 'description')