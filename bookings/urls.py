from django.urls import path
from .views import book_seat, bookings_success

urlpatterns = [
    path('', book_seat, name='bookings'),
    path('success/', bookings_success, name='bookings_success'),
]