from django.urls import path
from .views import book_seat

urlpatterns = [
    path('', book_seat, name='bookings'),
]