from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Seat
from films.models import Film, FilmSchedule
from .forms import FilmSelectForm, FilmScheduleForm

@login_required
def select_film(request):
    """
    Displays a form for film selection and redirects user to it
    schedules
    """
    if request.method == 'POST':
        form = FilmSelectForm(request.POST)
        if form.is_valid():
            film = form.cleaned_data['film']
            return redirect('film_schedules', film_id=film.id)
    else:
        form = FilmSelectForm()

    return render(request, 'select_film.html', {'form': form})

@login_required
def film_schedules(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    schedules = FilmSchedule.objects.filter(film=film)

    return render(request, 'select_schedule.html', {
        'film': film,
        'schedules': schedules,
    })


@login_required
def booking_page(request, schedule_id):
    """ 
    Handles the seat selection and creates booking for a film schedule
    """
    schedule = get_object_or_404(FilmSchedule, id=schedule_id)
    seats = Seat.objects.all()
    booked_seats = Booking.objects.filter(film_schedule=schedule).values_list('seat_id', flat=True)

    if request.method == 'POST':
        selected_seat_ids = request.POST.getlist('seats')  # list of Seat IDs

        if not selected_seat_ids:
            return render(request, 'book_seats.html', {
                'schedule': schedule,
                'seats': seats,
                'booked_seats': booked_seats,
                'error': "You must select at least one seat to finish booking."
            })

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


@login_required
def booking_success(request):
    """
    Confirmation page after booking 
    """

    return render(request, 'bookings_success.html')



# Admin/staff

# Staff Schedule Management (CRUD)

@staff_member_required
def manage_schedules(request):
    schedules = FilmSchedule.objects.select_related("film", "slot")
    return render(request, 'manage_schedules.html', {'schedules': schedules})


@staff_member_required
def schedule_create(request):
    if request.method == "POST":
        form = FilmScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_schedules')
    else:
        form = FilmScheduleForm()
    return render(request, 'schedule_form.html', {'form': form})


@staff_member_required
def schedule_update(request, pk):
    schedule = get_object_or_404(FilmSchedule, pk=pk)
    if request.method == "POST":
        form = FilmScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect("manage_schedules")
    else:
        form = FilmScheduleForm(instance=schedule)
    return render(request, 'schedule_form.html', {'form': form})


@staff_member_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(FilmSchedule, pk=pk)
    schedule.delete()
    return redirect('manage_schedules')



# Staff Booking Management (CRUD)

@staff_member_required
def manage_bookings(request):
    bookings = Booking.objects.select_related('film_schedule__film', 'seat', 'user')
    return render(request, 'manage_bookings.html', {'bookings': bookings})