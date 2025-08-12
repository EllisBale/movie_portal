from django.contrib import admin
from .models import Genre, Film, FilmSchedule, ShowtimeSlot
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


@admin.register(ShowtimeSlot)
class ShowtimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time',)
    ordering = ('start_time',)


@admin.register(FilmSchedule)
class FilmScheduleAdmin(admin.ModelAdmin):
    list_display = ('film', 'days_of_week', 'slot')
    list_filter = ('days_of_week', 'slot')
    
    def get_day_of_week(self, obj):
        return obj.get_days_of_week_display()
    get_day_of_week.short_description = 'Days of Week'