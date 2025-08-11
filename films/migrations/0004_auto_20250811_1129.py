from django.db import migrations
from datetime import time

def create_showtime_slots(apps, schema_editor):
    ShowtimeSlot = apps.get_model('films', 'ShowtimeSlot')
    times = [time(hour, 15) for hour in range(10, 22, 2)]
    for t in times:
        ShowtimeSlot.objects.get_or_create(start_time=t)

class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),  # change to your last migration file
    ]

    operations = [
        migrations.RunPython(create_showtime_slots),
    ]

