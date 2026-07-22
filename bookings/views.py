def booking_create(request):
    if request.method == 'POST':
        if request.POST.get('website'):
            return redirect('booking_success')

        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.customer = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form})