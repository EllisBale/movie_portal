from django.contrib import admin
from .models import Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'guests', 'date_booked',)
    list_filter = ('user', 'guests', 'date_booked', 'film')
    search_fields = ('date_booked', 'user', 'film')

    