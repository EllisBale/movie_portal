from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Seat
from films.models import Film, FilmSchedule
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


def film_schedules(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    schedules = FilmSchedule.objects.filter(film=film)

    return render(request, 'select_schedule.html', {
        'film': film,
        'schedules': schedules,
    })



def booking_page(request, schedule_id):
    schedule = get_object_or_404(FilmSchedule, id=schedule_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, schedule=schedule)
        if form.is_valid():
            seats = form.cleaned_data['seat_numbers']
            for seat_number in seats:
                seat = get_object_or_404(Seat, seat_number=seat_number)
                Booking.objects.create(
                    film_schedule=schedule,
                    seat=seat,
                    user=request.user
                )
            return redirect('booking_success')
    else:
        form = BookingForm(schedule=schedule)

    return render(request, 'book_seats.html', {
        'schedule': schedule,
        'form': form
    })



def booking_success(request):
    """ Confirmation page after booking """
    return render(request, 'booking_success.html') 