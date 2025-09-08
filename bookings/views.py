from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Seat
from films.models import Film, FilmSchedule
from .forms import FilmSelectForm

@login_required
def select_film(request):
    """
    Displays a form for film selection and redirects the user
    to the schedule page for the chosen film.
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
    """
    Shows all available schedules for the selected film.
    """
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
        # Check if no seats selected
        if not selected_seat_ids:
            return render(request, 'book_seats.html', {
                'schedule': schedule,
                'seats': seats,
                'booked_seats': booked_seats,
                'error': "You must select at least one seat to finish booking."
            })
        
        # Check for saet limit before creating bookings
        if len(selected_seat_ids) > 8:
            return render(request, 'book_seats.html', {
                'schedule': schedule,
                'seats': seats,
                'booked_seats': booked_seats,
                'error': "You can select a maximum of 8 seats."
            })
        
        # Check if seat already booked
        for seat_id in selected_seat_ids:
            if int(seat_id) in booked_seats:
                return render(request, 'book_seats.html', {
                    'schedule': schedule,
                    'seats': seats,
                    'booked_seats': booked_seats,
                    'error': f"Seat {seat_id} is already booked. Please choose another seat."
                })
            
        # Create bookings    
        for seat_id in selected_seat_ids:
            seat = get_object_or_404(Seat, id=seat_id)
            Booking.objects.create(film_schedule=schedule, seat=seat, user=request.user)
            
        return redirect('booking_success')

    return render(request, 'book_seats.html', {
        'schedule': schedule,
        'seats': seats,
        'booked_seats': booked_seats
    })


@login_required
def booking_success(request):
    """
    Displays a confirmation page after booking is successful.
    """

    return render(request, 'bookings_success.html')



@login_required
def user_booking(request):
    """
    Lists all bookings for the currently logged-in user.
    """
    booking_list = Booking.objects.filter(user=request.user).select_related('film_schedule__film', 'seat')
    return render(request, 'user_booking.html', {'booking_list': booking_list})



@login_required
def user_booking_delete(request, pk):
    """
    Deletes a users booking by its primary key
    and redirects back to the booking list.
    """
    bookings = get_object_or_404(Booking, pk=pk)
    bookings.delete()
    return redirect('user_bookings')