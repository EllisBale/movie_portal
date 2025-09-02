from django.urls import path
from .views import film_list, film_detail
from bookings.views import film_schedules

urlpatterns = [
    path('', film_list, name='films'),
    path('<int:film_id>/', film_detail, name='film_detail'),
    path('schedules/<int:film_id>/',  film_schedules, name='film_schedules'),
]