from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('', include('home.urls')),
    path('films/', include('films.urls')),
    path('menu/', include('menu.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('user_account.urls')),
    path('management/', include('management.urls')),
]
