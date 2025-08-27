from django.contrib import admin
from .models import Genre, Film, FilmSchedule, ShowtimeSlot


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ShowtimeSlot)
class ShowtimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time',)
    ordering = ('start_time',)

# FilmSchedule
class FilmScheduleInline(admin.TabularInline):
    model = FilmSchedule
    extra = 1
    fields = ('days_of_week', 'slot', 'specific_date', 'specific_time')

# Film admin
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'is_popular')
    list_filter = ('genre', 'is_popular', 'is_coming_soon', 'is_family')
    search_fields = ('title', 'cast', 'description')
    inlines = [FilmScheduleInline]

# FilmSchedule admin 
@admin.register(FilmSchedule)
class FilmScheduleAdmin(admin.ModelAdmin):
    list_display = ('film', 'display_schedule')
    list_filter = ('days_of_week', 'slot', 'specific_date')
    search_fields = ('film__title',)

    def display_schedule(self, obj):
        if obj.specific_date and obj.specific_time:
            return f"{obj.specific_date} at {obj.specific_time.strftime('%H:%M')}"
        elif obj.days_of_week is not None and obj.slot:
            day = dict(obj.DAYS_OF_WEEK).get(obj.days_of_week, 'Unknown day')
            return f"{day} at {obj.slot}"
        else:
            return "No schedule"
    
    display_schedule.short_description = 'Schedule'