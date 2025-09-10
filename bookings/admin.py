from django.contrib import admin
from .models import Booking, Seat


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'seat', 'film_schedule', 'booked_at')
    list_filter = ('film_schedule', 'booked_at')
    search_fields = (
        'user__username',
        'user__email',
        'seat__row',
        'seat__number')
    ordering = ('-booked_at',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('row', 'number')
    ordering = ('row', 'number')
