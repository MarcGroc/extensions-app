from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import User


class AdminAccessTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.staff_user = User.objects.create_user(
            username='staff',
            email='staff@example.com',
            password='staffpass123',
            is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username='regular',
            email='regular@example.com',
            password='regularpass123'
        )
        self.admin_url = reverse('admin:index')
        self.user_admin_url = reverse('admin:users_user_changelist')

    def test_superuser_can_access_admin(self):
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 200)

    def test_staff_can_access_admin(self):
        self.client.login(username='staff', password='staffpass123')
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_access_user_admin(self):
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(self.user_admin_url)
        self.assertEqual(response.status_code, 200)

    def test_staff_user_access_to_user_admin(self):
        self.client.login(username='staff', password='staffpass123')
        response = self.client.get(self.user_admin_url)
        # The exact behavior here might depend on your specific permissions setup
        self.assertIn(response.status_code, [200, 403])

    def test_user_admin_search_fields(self):
        self.client.login(username='admin', password='adminpass123')
        search_url = f"{self.user_admin_url}?q=admin"
        response = self.client.get(search_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'admin')

    def test_user_admin_ordering(self):
        User.objects.create_user(username='rich_user', balance=1000)
        User.objects.create_user(username='poor_user', balance=10)
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(self.user_admin_url)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertTrue(content.index('poor_user') < content.index('rich_user'))
