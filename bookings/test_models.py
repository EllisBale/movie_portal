from django.test import TestCase
from django.contrib.auth.models import User
from films.models import Film, FilmSchedule, Genre, ShowtimeSlot
from bookings.models import Seat, Booking
from datetime import date, time, timedelta


class TestSeatAndBookingModels(TestCase):
    def setUp(self):
        # Create genre and film
        self.genre = Genre.objects.create(name="Action")
        self.film = Film.objects.create(
            title="Test Film",
            description="Film description"
            cast="Actor1, Actor2",
            genre=self.genre,
            duration=125,
            poster="placeholder",
            release_date=date.today() - timedelta(days=1)
        )

        # Create film schedule
        self.slot = ShowtimeSlot.objects.create(start_time=(hour))