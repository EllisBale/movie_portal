from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from films.models import Film, Genre, FilmSchedule, ShowtimeSlot
from bookings.models import Booking, Seat
from menu.models import Menu
from datetime import date, time


User = get_user_model()


class TestManagementViews(TestCase):
    """
    Management views test.
    """

    def setUp(self):

        self.staff_user = User.objects.create_user(
            username="admin", password="password", is_staff=True
        )
        self.client.login(username="admin", password="password")

        self.genre = Genre.objects.create(name="Action")
        self.film = Film.objects.create(
            title="Test Film",
            description="Film description",
            cast="Actor1, Actor2",
            genre=self.genre,
            duration=120,
            poster="placeholder",
            release_date=date.today()
        )
        self.slot = ShowtimeSlot.objects.create(
            start_time=time(hour=18, minute=0))
        self.schedule = FilmSchedule.objects.create(
            film=self.film, days_of_week=0, slot=self.slot
            )
        self.seat = Seat.objects.create(row="A", number=1)
        self.booking = Booking.objects.create(
            film_schedule=self.schedule, seat=self.seat, user=self.staff_user
            )
        self.menu_item = Menu.objects.create(
            name="Burger", description="Yummy",
            category="food", image="placeholder")

    def test_manage_films_view(self):
        """
        Test that the films_list page returns 200 status code.
        """
        response = self.client.get(reverse('films_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/films_list.html')

    def test_film_create_view(self):
        """
        Test that the film_form page returns 200 status code.
        """
        response = self.client.get(reverse('film_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/film_form.html')

    def test_manage_schedules_view(self):
        """
        Test that the schedule page returns 200 status code.
        """
        response = self.client.get(reverse('schedule_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/schedule_list.html')

    def test_schedule_create_view(self):
        """
        Test that the schedule form page returns 200 status code.
        """
        response = self.client.get(reverse('schedule_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/schedule_form.html')

    def test_manage_bookings_view(self):
        """
        Test that the booking_list page returns 200 status code.
        """
        response = self.client.get(reverse('bookings_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/bookings_list.html')

    def test_manage_user_view(self):
        """
        Test that the user_list page returns 200 status code.
        """
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/user_list.html')

    def test_menu_create_view(self):
        """
        Test that the menu_form page returns 200 status code.
        """
        response = self.client.get(reverse('menu_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management/menu_form.html')
