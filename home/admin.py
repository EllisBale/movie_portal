from django.contrib import admin
from .models import PopularFilm

# Register your models here.

@admin.register(PopularFilm)
class PopularFilmAdmin(admin.ModelAdmin):
    list_display = ("title", "description")