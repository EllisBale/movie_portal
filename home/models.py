from django.db import models
from films.models import Film
# Create your models here.

class PopularFilm(models.Model):
    popular_films = Film.objects.filter(is_popular=True)
    