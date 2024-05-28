from rest_framework.test import APITestCase

from contact.api.views import ComingSoonViewSet, ContactViewSet
from contact.models import NewsletterSignup, Question


class TestContactViewSet(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.question = Question.objects.create(
            name="test",
            email="test@test.com",
            message="test",
            confirmation_sent=True
        )

    def test_create_question(self):
        # Test if question is created
        self.assertTrue(isinstance(self.question, Question))


class TestComingSoonViewSet(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.newsletter = NewsletterSignup.objects.create(
            name="test",
            email="test@test.com",
        )

    def test_create_newsletter(self):
        # Test if newsletter is created
        self.assertTrue(isinstance(self.newsletter, NewsletterSignup))