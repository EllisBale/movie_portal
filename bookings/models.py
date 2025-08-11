from django.conf import settings
from django.db import models
from films.models import FilmSchedule

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    film_schedule = models.ForeignKey(FilmSchedule, on_delete=models.CASCADE, related_name='bookings')
    guests = models.PositiveIntegerField(default=1)
    seat_number = models.CharField(max_length=10)

    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('film_schedule', 'seat_number')

    def __str__(self):
        return f"Booking for {self.user} - {self.film_schedule} seat {self.seat_number}"