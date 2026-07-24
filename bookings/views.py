from django.shortcuts import render, redirect
from .forms import BookingForm
from accounts.models import Vehicle

def booking_create(request):
    if request.method == 'POST':
        if request.POST.get('website'):
            return redirect('booking_success')

        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)

            selected_vehicle = form.cleaned_data.get('vehicle') if 'vehicle' in form.cleaned_data else None

            if selected_vehicle:
                booking.vehicle = selected_vehicle
                booking.vehicle_make = selected_vehicle.make
                booking.vehicle_model = selected_vehicle.model
                booking.vehicle_year = selected_vehicle.year
                booking.registration = selected_vehicle.registration
            elif request.user.is_authenticated and form.cleaned_data.get('vehicle_make'):
                # Logged-in customer entered a new vehicle manually — save it
                # to their account so it's available next time.
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
        form = BookingForm(user=request.user)

    return render(request, 'bookings/booking_form.html', {'form': form})


def booking_success(request):
    return render(request, 'bookings/booking_success.html')