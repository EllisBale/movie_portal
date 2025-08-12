from django.urls import path
from .views import bookings_success

urlpatterns = [
    path('', , name='bookings'),
    path('success/', bookings_success, name='bookings_success'),
]