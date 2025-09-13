from django.test import TestCase
from django.contrib.auth.models import User
from films.models import Film, FilmSchedule, Genre, ShowtimeSlot
from bookings.models import Seat, Booking
from datetime import date, time


class TestSeatAndBookingModels(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Action")
        self.film = Film.objects.create(
            title="Test Film",
            description="Film description",
            cast="Actor1, Actor2",
            genre=self.genre,
            duration=125,
            poster="placeholder",
            release_date=date.today()
        )

        # FilmSchedule
        self.slot = ShowtimeSlot.objects.create(
            start_time=time(hour=18, minute=0))
        self.schedule = FilmSchedule.objects.create(
            film=self.film,
            days_of_week=0,
            slot=self.slot
        )

        # User
        self.user = User.objects.create_user(
            username="testuser",
            password="Password"
        )

        # Seat
        self.seat = Seat.objects.create(row="A", number=1)

        # Booking
        self.booking = Booking.objects.create(
            film_schedule=self.schedule,
            seat=self.seat,
            user=self.user
        )

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "A1")

    def test_booking_str(self):
        self.assertEqual(
            str(self.booking),
            f"{self.user.username} - {self.seat} for {self.schedule}")
