from django.test import TestCase
from django.contrib.auth import get_user_model
from management.forms import FilmForm, StaffBookingForm, UserForm, MenuForm
from films.models import Genre, Film, FilmSchedule, ShowtimeSlot
from bookings.models import Seat
from menu.models import Menu
from datetime import date, time

User = get_user_model()


class TestManagementForms(TestCase):

    def setUp(self):
        # Minimal setup so forms can work
        self.genre = Genre.objects.create(name="Action")
        self.film = Film.objects.create(
            title="Test Film",
            description="Some description",
            cast="Actor1",
            genre=self.genre,
            release_date=date.today(),
            duration=120,
            poster="poster.jpg",
        )

        slot = ShowtimeSlot.objects.create(start_time=time(18, 0))

        self.seat = Seat.objects.create(row="A", number=1)
        self.schedule = FilmSchedule.objects.create(
            film=self.film,
            days_of_week=0,
            slot=slot,
            specific_date=date.today(),
            specific_time=time(19, 0)
        )
        self.user = User.objects.create(username="testuser")
        self.menu = Menu.objects.create(
            name="Burger",
            description="Delicious burger",
            image="burger.jpg",
            category="Food"
        )

    def test_film_form_valid(self):
        form = FilmForm(data={
            "title": "New Film",
            "description": "Description",
            "cast": "Actor1",
            "genre": self.genre.id,
            "release_date": date.today(),
            "duration": 100,
            "poster": "poster.jpg",
        })
        self.assertTrue(form.is_valid())

    def test_staff_booking_form_valid(self):
        form = StaffBookingForm(data={
            "film_schedule": self.schedule.id,
            "seat": self.seat.id,
            "user": self.user.id
        })
        self.assertTrue(form.is_valid())

    def test_user_form_valid(self):
        form = UserForm(data={
            "username": "newuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "is_active": True,
            "is_staff": False
        })
        self.assertTrue(form.is_valid())

    def test_menu_form_valid(self):
        form = MenuForm(data={
            'name': "Burger",
            'description': "Best burgers",
            'image': "placeholer",
            'category': "drink"
        })
        self.assertTrue(form.is_valid())