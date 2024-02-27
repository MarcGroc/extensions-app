from unittest import TestCase

from django.contrib.auth import get_user_model
from users.tasks import get_users_count

User = get_user_model()


class TesTasks(TestCase):
    def setUpTestData(cls):
        pass

    def test_returns_count(self):
        result = get_users_count()
        self.assertEqual(result, 0)
