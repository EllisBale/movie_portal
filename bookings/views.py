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
    """ Handles the seat selection and creates booking for a film schedule """
    schedule = get_object_or_404(FilmSchedule, id=schedule_id)
    seats = Seat.objects.all()
    booked_seats = Booking.objects.filter(film_schedule=schedule).values_list('seat_id', flat=True)

    if request.method == 'POST':
        selected_seat_ids = request.POST.getlist('seats')  # list of Seat IDs
        for seat_id in selected_seat_ids:
            seat = get_object_or_404(Seat, id=seat_id)  # always assigns seat
            Booking.objects.create(
                film_schedule=schedule,
                seat=seat,
                user=request.user
            )
        return redirect('booking_success')

    return render(request, 'book_seats.html', {
        'schedule': schedule,
        'seats': seats,
        'booked_seats': booked_seats
    })



def booking_success(request):
    """ Confirmation page after booking """
    return render(request, 'booking_success.html') 