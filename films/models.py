from django.db import models
from cloudinary.models import CloudinaryField
from datetime import date, time

class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    poster = CloudinaryField('image', default='placeholder')
    cast = models.TextField(
        help_text="Comma-separated list of actors"
    )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField(null=False, blank=False)
    duration = models.PositiveIntegerField(
        help_text="Total duration in minutes",
        null=False, blank=False
    )
    is_popular = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    is_family = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_duration_display(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        if hours:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"
    

class ShowtimeSlot(models.Model):
    start_time = models.TimeField(unique=True)

    def __str__(self):
        end_hour = (self.start_time.hour + 2) % 24
        end_time = time(hour=end_hour, minute=self.start_time.minute)
        return f"{self.start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"
    
class FilmSchedule(models.Model):
    
    DAYS_OF_WEEK = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
    ]


    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='schedules')
    days_of_week = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    slot = models.ForeignKey(ShowtimeSlot, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('days_of_week', 'slot')

    def __str__(self):
        day = dict(self.DAYS_OF_WEEK).get(self.days_of_week, 'Unknown day')
        return f"{self.film.title} on {day} at {self.slot}"
    

def save(self, *args, **kwargs):
    print(f"Attempting to save seat_number: {self.seat_number} (length: {len(self.seat_number)})")
    super().save(*args, **kwargs)