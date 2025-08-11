from django.contrib import admin
from .models import Booking, BookingSeat
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'guests', 'date_booked',)
    list_filter = ('user', 'guests', 'date_booked', 'film')
    search_fields = ('date_booked', 'user', 'film')
    ordering = ('-date', 'date_booked')

@admin.register(BookingSeat)
class BookingSeatAdmin(admin.ModelAdmin):
    list_display = ('booking', 'row', 'number')
    list_filter = ('row', 'booking')
    search_fields = ('booking__user__username', 'booking__film__title')