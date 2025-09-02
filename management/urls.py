from django.urls import path
from .views import film_create, film_delete, film_update, manage_films, manage_schedules, schedule_create, schedule_delete, manage_bookings, booking_update , booking_delete


urlpatterns = [
    path('films_list/', manage_films, name="films_list"),
    path('film_create/', film_create, name='film_create'),
    path('delete/<int:pk>/', film_delete, name='film_delete'),
    path('update/<int:pk>/', film_update, name='film_update'),

    path('schedule_list/', manage_schedules, name="schedule_list"),
    path('schedules/create/', schedule_create, name="schedule_create"),
    path('schedules/<int:pk>/delete/', schedule_delete, name="schedule_delete"),
    
    path('bookings_list/', manage_bookings, name="bookings_list"),
    path('bookings/<int:pk>/delete/', booking_delete, name="booking_delete"),
    path('bookings/<int:pk>/update/', booking_update, name="booking_update"),
]