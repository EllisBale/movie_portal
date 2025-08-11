from django.shortcuts import render, redirect
from .forms import BookingForm
# Create your views here.


def Bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = BookingForm()

    return render(request, 'bookings.html', {'form': form})