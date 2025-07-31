from django.contrib import admin
from .models import Genre, Film
# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'is_popular')
    list_filter = ('genre', 'is_popular', 'is_coming_soon', 'is_family')
    search_fields = ('title', 'cast', 'description')