from django.test import TestCase

from contact.models import NewsletterSignup, Question


class TestQuestionModel(TestCase):

    def setUp(self):
        self.question = Question.objects.create(
            name="Test",
            email="tst@test.com",
            message="Test message",
            confirmation_sent=True)

    def test_create_question(self):
        # Test if question is created
        self.assertTrue(isinstance(self.question, Question))


class TestNewsletterModel(TestCase):

    def setUp(self):
        self.newsletter = NewsletterSignup.objects.create(
            name="Test",
            email="tst@test.com",
            )

    def test_create_newsletter(self):
        # Test if newsletter is created
        self.assertTrue(isinstance(self.newsletter, NewsletterSignup))
