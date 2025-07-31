from django.db import models
from cloudinary.models import CloudinaryField

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