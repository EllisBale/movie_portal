from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from films.models import FilmSchedule
from .forms import BookingForm
from .models import Booking


def book_film_seat(request, schedule_id):
    schedule = get_object_or_404(FilmSchedule, id=schedule_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seat_numbers']

            for seat in seats:
                Booking.objects.create(
                    schedule=schedule,
                    seat_number=seat,
                    user=request.user
                )
            return redirect('bookings_success')
    else:
        form = BookingForm()

    return render(request, 'bookings/book_seats.html', {'form': form, 'schedule': schedule})
