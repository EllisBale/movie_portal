from django.db import models
from django.contrib.auth.models import User
from films.models import FilmSchedule


class Seat(models.Model):
    """
    Represents a single seat.
    """
    ROW_CHOICES = [(chr(i), chr(i)) for i in range(ord('A'), ord('F')+1)]
    row = models.CharField(max_length=1, choices=ROW_CHOICES)
    number = models.IntegerField()

    class Meta:
        unique_together = ('row', 'number')
        ordering = ['row', 'number']

    def __str__(self):
        return f"{self.row}{self.number}"


class Booking(models.Model):
    """
    Stores booking information for a specific seat and film schedule.
    """
    film_schedule = models.ForeignKey(
        FilmSchedule,
        on_delete=models.CASCADE,
        related_name='bookings'
        )

    seat = models.ForeignKey(
        Seat, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='bookings')

    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('film_schedule', 'seat')

    def __str__(self):
        return f"{self.user.username} - {self.seat} for {self.film_schedule}"
