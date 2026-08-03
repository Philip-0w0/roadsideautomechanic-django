import calendar
from datetime import date, datetime as dt
from django.shortcuts import render, redirect
from django.db import transaction
from django.db.models import Count, F, Q
from .forms import BookingForm
from .models import AvailabilitySlot, BookingRequest
from accounts.models import Vehicle


def get_available_slots(target_date=None):
    qs = AvailabilitySlot.objects.filter(
        is_blocked=False,
    ).annotate(
        booked_count=Count('bookingrequest', filter=~Q(bookingrequest__status='cancelled'))
    ).filter(booked_count__lt=F('max_bookings'))
    if target_date:
        qs = qs.filter(date=target_date)
    return qs


def build_calendar(year, month, selected_date):
    cal = calendar.Calendar(firstweekday=0)
    available_dates = set(
        get_available_slots().filter(date__year=year, date__month=month).values_list('date', flat=True)
    )
    weeks = []
    for week in cal.monthdatescalendar(year, month):
        week_data = []
        for day in week:
            week_data.append({
                'date': day,
                'in_month': day.month == month,
                'has_availability': day in available_dates and day >= date.today(),
                'is_selected': day == selected_date,
            })
        weeks.append(week_data)
    return weeks


def booking_create(request):
    today = date.today()

    selected_date_str = request.GET.get('date') or request.POST.get('selected_date')
    selected_date = None
    if selected_date_str:
        try:
            selected_date = dt.strptime(selected_date_str, '%Y-%m-%d').date()
        except ValueError:
            pass

    if selected_date:
        year, month = selected_date.year, selected_date.month
    else:
        try:
            year = int(request.GET.get('year', today.year))
            month = int(request.GET.get('month', today.month))
        except ValueError:
            year, month = today.year, today.month

    calendar_weeks = build_calendar(year, month, selected_date)
    day_slots = get_available_slots(target_date=selected_date) if selected_date else AvailabilitySlot.objects.none()

    if request.method == 'POST':
        if request.POST.get('website'):
            return redirect('booking_success')

        form = BookingForm(request.POST, user=request.user, available_slots=day_slots)
        if form.is_valid():
            with transaction.atomic():
                slot = form.cleaned_data['slot']
                fresh_slot = AvailabilitySlot.objects.select_for_update().get(id=slot.id)
                current_count = fresh_slot.bookingrequest_set.exclude(status='cancelled').count()

                if current_count >= fresh_slot.max_bookings:
                    form.add_error('slot', 'Sorry, that time was just booked. Please choose another.')
                else:
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
        form = BookingForm(user=request.user, available_slots=day_slots)

    prev_month, prev_year = (month - 1, year) if month > 1 else (12, year - 1)
    next_month, next_year = (month + 1, year) if month < 12 else (1, year + 1)

    return render(request, 'bookings/booking_form.html', {
        'form': form,
        'calendar_weeks': calendar_weeks,
        'month_name': calendar.month_name[month],
        'year': year, 'month': month,
        'selected_date': selected_date,
        'day_slots': day_slots,
        'prev_month': prev_month, 'prev_year': prev_year,
        'next_month': next_month, 'next_year': next_year,
    })


def booking_success(request):
    return render(request, 'bookings/booking_success.html')