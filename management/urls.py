from django.urls import path
from .views import film_create, film_delete, film_update, manage_films, manage_schedules, schedule_create, schedule_delete, manage_bookings, booking_update , booking_delete, manage_user, user_delete, user_update, menu_update, menu_delete, menu_create, schedule_update


urlpatterns = [
    # Films
    path('films_list/', manage_films, name="films_list"),
    path('film_create/', film_create, name='film_create'),
    path('delete/<int:pk>/', film_delete, name='film_delete'),
    path('update/<int:pk>/', film_update, name='film_update'),
    # Schedule
    path('schedule_list/', manage_schedules, name="schedule_list"),
    path('schedules/create/', schedule_create, name="schedule_create"),
    path('schedules/<int:pk>/delete/', schedule_delete, name="schedule_delete"),
    path('schedules/<int:pk>/edit/', schedule_update, name="schedule_update"),
    # Booking
    path('bookings_list/', manage_bookings, name="bookings_list"),
    path('bookings/<int:pk>/delete/', booking_delete, name="booking_delete"),
    path('bookings/<int:pk>/update/', booking_update, name="booking_update"),
    # User
    path('user_list/', manage_user, name="user_list"),
    path('user_list/<int:pk>/delete/', user_delete, name="user_delete"),
    path('user_list/<int:pk>/edit/', user_update, name="user_update"),

    # Menu
    path('menu/create/', menu_create, name='menu_create'),
    path('menu/<int:pk>update/', menu_update, name='menu_update'),
    path('menu/<int:pk>delete/', menu_delete, name='menu_delete'),
]