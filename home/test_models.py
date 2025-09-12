from django.test import TestCase
from datetime import date, timedelta
from films.models import Film, Genre


class TestHomeBooleans(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Action")

        self.popular_film = Film.objects.create(
            title="Jack Pond",
            description="film description",
            cast="Actor1, Actor2",
            genre=self.genre,
            duration=125,
            poster="placeholder",
            release_date=date.today() - timedelta(days=1),
            is_popular=True,
            is_coming_soon=False
        )

        self.coming_soon_film = Film.objects.create(
            title="Coming soon movie",
            description="coming soon film",
            cast="Actor1, Actor2",
            genre=self.genre,
            duration=125,
            poster="placeholder",
            release_date=date.today() + timedelta(days=10),
            is_popular=False,
            is_coming_soon=True
        )

    def test_is_popular_film(self):
        self.assertTrue(self.popular_film.is_popular)
        self.assertFalse(self.popular_film.is_coming_soon)


    def test_is_coming_soon(self):
        self.assertTrue(self.coming_soon_film.is_coming_soon)
        self.assertFalse(self.coming_soon_film.is_popular)
