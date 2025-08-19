from django.db import models
from films.models import Film
# Create your models here.

class PopularFilm(models.Model):
    popular_films = Film.objects.filter(is_popular=True)
    
class CommingSoon(models.Model):
    comming_soon = Film.objects.filter(is_coming_soon=True)


    