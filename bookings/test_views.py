from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from films.models import Film, Genre, ShowtimeSlot, FilmSchedule
from bookings.models import Seat, Booking
from datetime import date, time


class TestBookingViews(TestCase):
    """
    Booking views test.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="Password123")
        self.client.login(username="testuser", password="Password123")

        genre = Genre.objects.create(name="Action")
        film = Film.objects.create(
            title="Test Film",
            description="Description",
            cast="Actor1, Actor2",
            genre=genre,
            duration=120,
            poster="placeholder",
            release_date=date.today()
        )
        slot = ShowtimeSlot.objects.create(start_time=time(hour=18, minute=0))
        self.schedule = FilmSchedule.objects.create(
            film=film, days_of_week=0, slot=slot
            )

        self.film_id = film.id
        self.schedule_id = self.schedule.id

        self.seat = Seat.objects.create(row="A", number=1)
        self.booking = Booking.objects.create(
            film_schedule=self.schedule,
            seat=self.seat,
            user=self.user
        )

    def test_select_film_view(self):
        """
        Test that the select_film page returns 200 status code.
        """
        response = self.client.get(reverse('select_film'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'select_film.html')

    def test_film_schedules_view(self):
        """
        Test that the select_schedule page returns 200 status code.
        """
        response = self.client.get(reverse(
            'film_schedules', args=[self.film_id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'select_schedule.html')

    def test_booking_seat_view(self):
        """
        Test that the booking_seat page returns 200 status code.
        """
        response = self.client.get(reverse(
            'booking_seat', args=[self.schedule_id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_seats.html')

    def test_booking_success_view(self):
        """
        Test that the booking_success page returns 200 status code.
        """
        response = self.client.get(reverse('booking_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings_success.html')

    def test_user_bookings_view(self):
        """
        Test that the user_booking page returns 200 status code.
        """
        response = self.client.get(reverse('user_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_booking.html')

    def test_user_booking_delete_view(self):
        """
        Test that the user_booking_delete returns 302
        """
        response = self.client.get(reverse(
            'user_booking_delete', args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 302)
