from django.test import TestCase
from django.urls import reverse


class TestMenuViews(TestCase):
    """
    Menu views test.
    """

    def test_get_menu_page(self):
        """
        Test that the menu list returns 200 status code.
        """
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        