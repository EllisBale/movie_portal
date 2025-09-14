from django.urls import path
from bookings.views import *


urlpatterns = [
    path('select-film/', select_film, name='select_film'),
    path(
        'film/<int:film_id>/schedules/',
        film_schedules, name='film_schedules'),

    path('<int:schedule_id>/', booking_seat, name='booking_seat'),
    path('success/', booking_success, name='booking_success'),
    path('my_bookings/', user_booking, name='user_bookings'),
    path(
        'my_bookings/delete/<int:pk>/',
        user_booking_delete, name='user_booking_delete'),
]
