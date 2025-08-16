from django.urls import path
from .views import booking_page, book_seat, booking_success, booking_page, select_film

urlpatterns = [
    path('select-film/', select_film, name='select_film'),
    path('<int:schedule_id>/', booking_page, name='booking_page'),  
    path('<int:schedule_id>/book/<int:seat_id>/', book_seat, name='book_seat'),
    path('success/', booking_success, name='bookings_success'),
]