from django.urls import path
from .views import index, film_family

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('family/', film_family, name='family'),
]