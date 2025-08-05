from django.urls import path
from .views import film_list, film_detail

urlpatterns = [
    path('', film_list, name='films'),
    path('<int:film_id>/', film_detail, name='film_detail'),
]