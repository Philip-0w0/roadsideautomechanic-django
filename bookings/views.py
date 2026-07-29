from django.shortcuts import render, redirect
from django.db import transaction
from django.db.models import Count, F
from .forms import BookingForm
from .models import AvailabilitySlot
from accounts.models import Vehicle

def get_available_slots():
    return AvailabilitySlot.objects.filter(
        is_blocked=False,
    ).annotate(
        booked_count=Count('bookingrequest')
    ).filter(booked_count__lt=F('max_bookings'))


def booking_create(request):
    available_slots = get_available_slots()

    if request.method == 'POST':
        if request.POST.get('website'):
            return redirect('booking_success')

        form = BookingForm(request.POST, user=request.user, available_slots=available_slots)
        if form.is_valid():
            with transaction.atomic():
                # Re-check the slot is still available right before saving —
                # closes the gap between page load and submission.
                slot = form.cleaned_data['slot']
                fresh_slot = AvailabilitySlot.objects.select_for_update().get(id=slot.id)
                current_count = fresh_slot.bookingrequest_set.count()

                if current_count >= fresh_slot.max_bookings:
                    form.add_error('slot', 'Sorry, that time was just booked. Please choose another.')
                    return render(request, 'bookings/booking_form.html', {'form': form})

                booking = form.save(commit=False)
                booking.slot = fresh_slot

                selected_vehicle = form.cleaned_data.get('vehicle') if 'vehicle' in form.cleaned_data else None
                if selected_vehicle:
                    booking.vehicle = selected_vehicle
                    booking.vehicle_make = selected_vehicle.make
                    booking.vehicle_model = selected_vehicle.model
                    booking.vehicle_year = selected_vehicle.year
                    booking.registration = selected_vehicle.registration
                elif request.user.is_authenticated and form.cleaned_data.get('vehicle_make'):
                    new_vehicle = Vehicle.objects.create(
                        owner=request.user,
                        make=form.cleaned_data['vehicle_make'],
                        model=form.cleaned_data['vehicle_model'],
                        year=form.cleaned_data['vehicle_year'],
                        registration=form.cleaned_data.get('registration', ''),
                    )
                    booking.vehicle = new_vehicle

                if request.user.is_authenticated:
                    booking.customer = request.user

                booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm(user=request.user, available_slots=available_slots)

    return render(request, 'bookings/booking_form.html', {'form': form})


def booking_success(request):
    return render(request, 'bookings/booking_success.html')