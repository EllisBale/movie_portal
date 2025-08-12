from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
# Create your views here.

@login_required
def book_seat(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bookings_success')
    else:
        form = BookingForm()
    return render(request, 'bookings.html', {'form': form})


def bookings_success(request):
    return render(request, 'bookings_success.html')