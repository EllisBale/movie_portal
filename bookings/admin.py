from django.contrib import admin
from .models import Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'film_schedule', 'guests', 'seat_number', 'booked_at')
    search_fields = ('user__username', 'film_schedule__film__title', 'seat_number')
    list_filter = ('film_schedule__show_date',)

