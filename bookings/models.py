from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from films.models import Film

# Create your models here.

def validate_not_past_date(current_date):
    if current_date < timezone.localdate():
        raise ValidationError("Booking date cannot be in the past.")
    

class Booking(models.Model):
    """Dynamically generate times between 10am and midnight""" 

    TIME_CHOICES = [
        (f"{h}am", f"{h}am") if h < 12 else
        (f"{h - 12 if h > 12 else 12}pm", f"{h - 12 if h > 12 else 12}pm")
        for h in range(10, 24)
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=timezone.now, validators=[validate_not_past_date])
    time = models.CharField(max_length=5, choices=TIME_CHOICES, default="10am")
    guests = models.PositiveIntegerField(default=1)
    date_booked = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'user']

    def __str__(self):
        return f"Booking for {self.film} on {self.date} at {self.time} by {self.user}"
    


class BookingSeat(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='seats'
    )

    ROW_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]

    row = models.CharField(max_length=2, choices=ROW_CHOICES)
    number = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )

    class Meta:
        unique_together = ('row', 'number', 'booking')

    def __str__(self):
        return f"Seat {self.row}{self.number} for {self.booking}"