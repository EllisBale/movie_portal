from django.urls import path
from .views import user_list

urlpatterns = [
    path("users_list/", user_list, name="users"),
]