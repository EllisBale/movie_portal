from django.shortcuts import redirect
from .models import Booking

def book_seat(request, schedule_id, seat_id):
    if not request.user.is_authenticated:
        return redirect('login')

    Booking.objects.create(
        film_schedule_id=schedule_id,
        seat_id=seat_id,
        user=request.user
    )
    return redirect('booking_success')


def booking_success(request):
    
    return redirect('bookings_success')