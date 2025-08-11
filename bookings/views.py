from django.shortcuts import render
from .models import Booking
# Create your views here.


def Bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})