from django.contrib import admin
from .models import Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'schedule', 'user', 'booked_at')
    list_filter = ('schedule', 'booked_at')
    search_fields = ('seat_number', 'user__username', 'user__email')
    ordering = ('-booked_at',)