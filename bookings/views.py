from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking, BookingSeat
# Create your views here.

@login_required
def book_seat(request):
    """
    Handles the booking of seats for a film screening
    """
 


def bookings_success(request):
    """
    A simple view to display booking message
    """
    return render(request, 'bookings_success.html')