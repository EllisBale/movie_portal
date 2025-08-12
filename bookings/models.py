from django.db import models
from django.conf import settings
from films.models import FilmSchedule
from .seats import validate_seat


class Booking(models.Model):
    schedule = models.ForeignKey(
        FilmSchedule,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    seat_number = models.CharField(
        max_length=3,
        validators=[validate_seat]
    )
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('schedule', 'seat_number')
        ordering = ['schedule', 'seat_number']

    def __str__(self):
        return f"{self.seat_number} - {self.schedule}"
