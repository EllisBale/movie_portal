from django.urls import path
from home.views import *

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('family/', film_family, name='family'),
]
