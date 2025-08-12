from django.urls import path
from .views import book_film_seat, booking_success

urlpatterns = [
    path('', book_film_seat, name='bookings'),
    path('success/', booking_success, name='bookings_success'),
]