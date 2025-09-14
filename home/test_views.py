from django.test import TestCase
from django.urls import reverse


class TestHomeViews(TestCase):
    """
    Test for home page.
    """
    def test_home_page(self):
        """
        Test if home page returns status code 200.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

