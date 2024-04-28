from django.test import TestCase
from django.urls import reverse

from users.models import User


class TestUser(TestCase):
    """Test class for User model"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(name="test-name", first_name="test-first", last_name="test-last")

    def test_user_fields(self):
        self.assertEqual(self.user.name, "test-name")
        self.assertEqual(self.user.first_name, "test-first")
        self.assertEqual(self.user.last_name, "test-last")

    def test_get_absolute_url(self):
        user = User.objects.get(name="test-name")
        expected_url = reverse("users:detail", kwargs={"username": user.name})
        self.assertEqual(user.get_absolute_url(), expected_url)
