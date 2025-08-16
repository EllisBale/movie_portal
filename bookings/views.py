from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Seat
from films.models import FilmSchedule
from .forms import BookingForm, FilmSelectForm


def select_film(request):
    if request.method == 'POST':
        form = FilmSelectForm(request.POST)
        if form.is_valid():
            film = form.cleaned_data['film']
            return redirect('film_schedules', film_id=film.id)
    else:
        form = FilmSelectForm()

    return render(request, 'select_film.html', {'form': form})




def booking_page(request, schedule_id):
    """Show available seats for a specific film schedule."""
    schedule = get_object_or_404(FilmSchedule, id=schedule_id)
    seats = Seat.objects.all()
    booked_seats = Booking.objects.filter(film_schedule=schedule).values_list('seat_id', flat=True)

    context = {
        'schedule': schedule,
        'seats': seats,
        'booked_seats': booked_seats,
    }
    return render(request, 'book_seats.html', context)  


def book_seat(request, schedule_id, seat_id):
    """ Book a seat for logged in user """
    if not request.user.is_authenticated:
        return redirect('login')

    schedule = get_object_or_404(FilmSchedule, id=schedule_id)
    seat = get_object_or_404(Seat, id=seat_id)

    if Booking.objects.filter(film_schedule=schedule, seat=seat).exists():
        seats = Seat.objects.all()
        booked_seats = Booking.objects.filter(film_schedule=schedule).values_list('seat_id', flat=True)
        return render(request, 'book_seats.html', {  
            'schedule': schedule,
            'seats': seats,
            'booked_seats': booked_seats,
            'error': f"Seat {seat} is already booked.",
        })

    Booking.objects.create(
        film_schedule=schedule,
        seat=seat,
        user=request.user
    )

    return redirect('booking_success')


def booking_success(request):
    """ Confirmation page after booking """
    return render(request, 'booking_success.html') 