from django.urls import path
from .views import testbooking

urlpatterns = [
    path('', testbooking, name='test'),
    
]