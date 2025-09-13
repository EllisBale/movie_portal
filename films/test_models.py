from django.test import TestCase
from django.utils import timezone
from datetime import date, timedelta
from films.models import Film, Genre


class TestFilmModel(TestCase):
    """
    Test for Film model.
    """
    def setUp(self):
        self.genre = Genre.objects.create(name="Action")
        self.common_film_data = {
            "title": "Jack Pond",
            "description": "film description",
            "cast": "Actor1, Actor2",
            "genre": self.genre,
            "duration": 125,
            "poster": "placeholder"
        }

    def test_film_str_returns_title(self):
        """
        Test that the Film __str__ returns the film title.
        """
        film = Film.objects.create(
            **self.common_film_data,
            release_date=date.today()

        )
        self.assertEqual(str(film), "Jack Pond")

    def test_get_duration_display_hours_and_minutes(self):
        """
        Test that get_duration_display returns in hours and minutes.
        """
        film = Film.objects.create(
            **self.common_film_data,
            release_date=date.today()
        )
        self.assertEqual(film.get_duration_display(), "2h 5m")

    def test_is_coming_soon(self):
        """
        Test that a film with a future release_date is marked as coming soon.
        """
        future_date = date.today() + timedelta(days=10)
        film = Film.objects.create(
            **self.common_film_data,
            release_date=future_date
        )
        self.assertTrue(film.is_coming_soon)

    def test_is_family_true(self):
        """
        Test that is_family boolean field is correctly stored as True.
        """
        film = Film.objects.create(
            **self.common_film_data,
            release_date=date.today(),
            is_family=True
        )
        self.assertTrue(film.is_family)

    def test_is_hero_image_true(self):
        """
        Test that is_hero_image boolean field is correctly stored as True.
        """
        film = Film.objects.create(
            **self.common_film_data,
            release_date=date.today(),
            is_hero_image=True
        )
        self.assertTrue(film.is_hero_image)
