from django.urls import path
from .views import film_list, film_detail, film_create, film_delete, film_update, manage_films
from bookings.views import film_schedules

urlpatterns = [
    path('', film_list, name='films'),
    path('<int:film_id>/', film_detail, name='film_detail'),
    path('schedules/<int:film_id>/',  film_schedules, name='film_schedules'),
    path('create/',  film_create, name='film_create'),
    path('delete/<int:pk>/',  film_delete, name='film_delete'),
    path('update/<int:pk>/',  film_update, name='film_update'),
    path('manage/', manage_films, name="manage_films"),
]