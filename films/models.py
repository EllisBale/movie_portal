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
    is_hero_image = models.BooleanField(default=False)

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
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='schedules')
    
    # Film schedule days
    DAYS_OF_WEEK = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]
    days_of_week = models.IntegerField(choices=DAYS_OF_WEEK, null=True, blank=True)
    slot = models.ForeignKey(ShowtimeSlot, on_delete=models.CASCADE, null=True, blank=True)
    
    # Specific schedule
    specific_date = models.DateField(null=True, blank=True)
    specific_time = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ('film', 'days_of_week', 'slot', 'specific_date', 'specific_time')

    def __str__(self):
        if self.specific_date and self.specific_time:
            return f"{self.film.title} on {self.specific_date} at {self.specific_time.strftime('%H:%M')}"
        else:
            day = dict(self.DAYS_OF_WEEK).get(self.days_of_week, 'Unknown day')
            return f"{self.film.title} on {day} at {self.slot}"