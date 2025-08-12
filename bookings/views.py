from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking

@login_required
def book_film_seat(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            schedule = form.cleaned_data['schedule']  # get selected showtime slot
            seats = form.cleaned_data['seat_numbers']
            for seat in seats:
                Booking.objects.create(schedule=schedule, seat_number=seat, user=request.user)
            return redirect('bookings_success')
    else:
        form = BookingForm()

    return render(request, 'book_seats.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings_success.html')
