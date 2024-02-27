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

    def test_admin_list_display(self):
        # Ensure superuser can see the list view with correct fields
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('admin:users_user_changelist'))
        self.assertContains(response, 'username')
        self.assertContains(response, 'name')
        self.assertContains(response, 'email')
        self.assertContains(response, 'is_superuser')

    def test_admin_search(self):
        # Ensure the search functionality works
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('admin:users_user_changelist') + '?q=Regular')
        self.assertContains(response, 'Regular User')
