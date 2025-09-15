from django.test import TestCase
from bookings.forms import BookingForm
from bookings.seats import ALL_SEATS
from films.models import Film, Genre, FilmSchedule, ShowtimeSlot
from datetime import date, time


class TestBookingForm(TestCase):
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
        self.slot = ShowtimeSlot.objects.create(
            start_time=time(hour=18, minute=0))
        self.schedule = FilmSchedule.objects.create(
            film=self.film, days_of_week=0, slot=self.slot
        )

    def test_booking_form_valid(self):
        """
        Test valid BookingForm with seats selected.
        """
        form = BookingForm(
            data={'schedule': self.schedule.id, 'seat_numbers': ALL_SEATS[:2]},
            schedule=self.schedule
        )
        self.assertTrue(form.is_valid())
