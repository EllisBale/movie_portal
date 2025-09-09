from django.urls import path
from .views import profile_update, profile_view, change_password

urlpatterns = [
    path('', profile_view, name='profile'),
    path('update/', profile_update, name='profile_update'),
    path('change_password/', change_password, name='change_password'),
]