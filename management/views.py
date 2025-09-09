from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required


# Models
from films.models import Film
from films.models import FilmSchedule
from bookings.models import Booking
from menu.models import Menu


# Forms
from .forms import FilmForm, StaffBookingForm, UserForm, MenuForm
from bookings.forms import FilmScheduleForm


User = get_user_model()

# ----------------------------
#   Film Management (CRUD)
# ----------------------------

@staff_member_required
def manage_films(request):
    """
    Displays a list of all films for staff management.
    """
    films_list = Film.objects.all().order_by("title")
    return render(request, "management/films_list.html", {"films_list": films_list})


@staff_member_required
def film_create(request):
    """
    Allow staff to create a new film.
    """
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films_list')
    else:
        form = FilmForm()
    return render(request, 'management/film_form.html', {'form': form})


@staff_member_required
def film_update(request, pk):
    """
    Allow staff to edit details of existing films.
    """
    film = get_object_or_404(Film, pk=pk)
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect("films_list")
    else:
        form = FilmForm(instance=film)
    return render(request, 'management/film_form.html', {'form': form})


@staff_member_required
def film_delete(request, pk):
    """
    Allow staff to delete a film.
    """
    film = get_object_or_404(Film, pk=pk)
    film.delete()
    return redirect('films_list')

# ----------------------------
#  Schedule Management (CRUD) 
# ----------------------------

@staff_member_required
def manage_schedules(request):
    """
    Display a list of all film schedules for staff management.
    """
    schedule_list = FilmSchedule.objects.select_related("film", "slot")
    return render(request, 'management/schedule_list.html', {'schedule_list': schedule_list})


@staff_member_required
def schedule_create(request):
    """
    Allow staff to create a new film schedule.
    """
    if request.method == "POST":
        form = FilmScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = FilmScheduleForm()
    return render(request, 'management/schedule_form.html', {'form': form})


@staff_member_required
def schedule_update(request, pk):
    """
    Allow staff to update details of an existing film schedule.
    """
    schedule = get_object_or_404(FilmSchedule, pk=pk)
    if request.method == "POST":
        form = FilmScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect("schedule_list")
    else:
        form = FilmScheduleForm(instance=schedule)
    return render(request, 'management/schedule_form.html', {'form': form})


@staff_member_required
def schedule_delete(request, pk):
    """
    Allow staff to delete a film schedule.
    """
    schedule = get_object_or_404(FilmSchedule, pk=pk)
    schedule.delete()
    return redirect('schedule_list')


# ----------------------------
#  Booking Management (Edit and delete) 
# ----------------------------

@staff_member_required
def manage_bookings(request):
    """
    Display a list of all bookings for staff management.
    """
    bookings_list = Booking.objects.select_related('film_schedule__film', 'seat', 'user')
    return render(request, 'management/bookings_list.html', {'bookings_list': bookings_list})


@staff_member_required
def booking_update(request, pk):
    """
    Allow staff to update an existing booking.
    """
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = StaffBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("bookings_list")
    else:
        form = StaffBookingForm(instance=booking)
    return render(request, 'management/booking_update.html', {'form': form})
        
@staff_member_required
def booking_delete(request, pk):
    """
    Allow staff to delete a booking
    """
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    return redirect('bookings_list')

# ----------------------------
# User Management (CRUD)
# ----------------------------

@staff_member_required
def manage_user(request):
    """
    Display a list of all registered users for staff management.
    """
    users = User.objects.all()
    return render(request, 'management/user_list.html', {'users': users})


@staff_member_required
def user_delete(request, pk):
    """
    Allow staff to delete a user.
    """
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user_list')


@staff_member_required
def user_update(request, pk):
    """
    Allow staff to update user information.
    """
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'management/user_form.html', {'form': form})


# ----------------------------
# Menu Management (CRUD)
# ----------------------------

@staff_member_required
def menu_create(request):
    """
    Allow staff to create a new menu item.
    """
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('menu')
    else:
        form = MenuForm()
    return render(request, 'management/menu_form.html', {'form': form})


@staff_member_required
def menu_update(request, pk):
    """
    Allow staff to update an existing menu item.
    """
    item = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuForm(instance=item)
    
    return render(request, 'management/menu_form.html', {'form': form})


@staff_member_required
def menu_delete(request, pk):
    """
    Allow staff to delete a menu item.
    """
    item = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        item.delete()
    return redirect('menu')
    

