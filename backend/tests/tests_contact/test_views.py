from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from contact.models import NewsletterSignup, Question


class ContactViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:contact-list')

    @patch('contact.tasks.send_confirmation_email.delay')
    def test_create_contact(self, mock_send_confirmation):
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "message": "This is a test message."
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)
        question = Question.objects.first()
        self.assertEqual(question.name, data['name'])
        self.assertEqual(question.email, data['email'])
        self.assertEqual(question.message, data['message'])

        # Check if the Celery task was called
        mock_send_confirmation.assert_called_once_with(question.id)

    def test_create_contact_invalid_data(self):
        data = {
            "name": "John Doe",
            "email": "invalid-email",
            "message": ""
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Question.objects.count(), 0)

    def test_get_method_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class TestNewsletterSignup(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:coming-soon-list')

    @patch('contact.tasks.newsletter_signup.delay')
    def test_create_newsletter_signup(self, mock_newsletter_signup):
        data = {
            "name": "John Doe",
            "email": "john@example.com",
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NewsletterSignup.objects.count(), 1)
        newsletter_signup = NewsletterSignup.objects.first()
        self.assertEqual(newsletter_signup.email, data['email'])

        mock_newsletter_signup.assert_called_once_with(newsletter_signup.id)

    def test_create_newsletter_signup_invalid_data(self):
        data = {
            "email": "invalid-email",
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(NewsletterSignup.objects.count(), 0)

    def test_get_method_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)