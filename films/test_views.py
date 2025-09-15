from django.test import TestCase
from django.urls import reverse


class TestFilmViews(TestCase):
    """
    Test for Film page
    """

    def test_film_page(self):
        """
        Test that film page returns status code 200.
        """
        response = self.client.get(reverse('films'))
        self.assertEqual(response.status_code, 200)
