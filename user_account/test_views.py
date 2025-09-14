from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestUserAccountViews(TestCase):
    """
    Test user_account views.
    """
    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(
            username="testuser",
            password="Password123"
        )
        self.client.login(username="testuser", password="Password123")

    def test_profile_view(self):
        """Test profile page returns 200 and correct template."""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_account/profile.html')

    def test_profile_update_view_get(self):
        """Test GET request for profile_update view."""
        response = self.client.get(reverse('profile_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_account/profile_update.html')

    def test_change_password_view_get(self):
        """Test GET request for change_password view."""
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_account/change_password.html')
