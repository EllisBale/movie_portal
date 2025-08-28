from django.urls import path
from .views import booking_page, select_film, booking_success, booking_page, film_schedules, manage_schedules, schedule_create, schedule_update, schedule_delete, manage_bookings, booking_update , booking_delete



urlpatterns = [
    path('select-film/', select_film, name='select_film'),
    path('film/<int:film_id>/schedules/', film_schedules, name='film_schedules'),
    path('<int:schedule_id>/', booking_page, name='booking_page'),
    path('success/', booking_success, name='booking_success'),
    path('manage/schedules/', manage_schedules, name="manage_schedules"),
    path('manage/schedules/create', schedule_create, name="schedule_create"),
    path('manage/schedules/<int:pk>/delete/', schedule_delete, name="schedule_delete"),
    path('manage/bookings/', manage_bookings, name="manage_bookings"),
    path('manage/bookings/<int:pk>/delete', booking_delete, name="booking_delete"),
    path('manage/bookings/<int:pk>/update', booking_update, name="booking_update"),
  
]