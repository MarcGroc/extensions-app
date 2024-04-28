from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class UserAdminTest(TestCase):
    """Test case for the user admin page."""

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123",
        )
        cls.user = User.objects.create_user(
            username="user",
            email="user@example.com",
            password="user123",
            name="Regular User",
        )
        cls.client = Client()

    def test_admin_access(self):
        # Non-superusers should not access the User admin
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('admin:app_list', args=('auth',)))
        self.assertEqual(response.status_code, (302 or 403))  # Redirects or forbidden

        # Superusers should access the User admin
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('admin:app_list', args=('auth',)))
        self.assertEqual(response.status_code, 200)

