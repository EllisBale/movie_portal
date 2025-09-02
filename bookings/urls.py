from django.urls import path
from .views import booking_page, select_film, booking_success, booking_page, film_schedules



urlpatterns = [
    path('select-film/', select_film, name='select_film'),
    path('film/<int:film_id>/schedules/', film_schedules, name='film_schedules'),
    path('<int:schedule_id>/', booking_page, name='booking_page'),
    path('success/', booking_success, name='booking_success'),
]