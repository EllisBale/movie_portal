from django.urls import path
from .views import Bookings

urlpatterns = [
    path('', Bookings, name='bookings'),
]