from unittest.mock import patch

from django.test import TestCase

from contact.models import Question


class QuestionSignalTests(TestCase):
    @patch('contact.tasks.send_confirmation_email.delay')
    def test_send_confirmation_email_called(self, mock_send_confirmation_email):
        # Tworzenie instancji modelu Question bez ustawienia `confirmation_sent`
        question = Question.objects.create(
            name="Test User",
            email="test@example.com",
            message="Test message"
        )

        # Sprawdzamy, czy `send_confirmation_email.delay` zostało wywołane
        mock_send_confirmation_email.assert_called_once_with(question.id)

    @patch('contact.tasks.send_confirmation_email.delay')
    def test_send_confirmation_email_not_called(self, mock_send_confirmation_email):
        # Tworzenie instancji modelu Question z ustawionym `confirmation_sent`
        question = Question.objects.create(
            name="Test User",
            email="test@example.com",
            message="Test message",
            confirmation_sent=True
        )

        # Sprawdzamy, czy `send_confirmation_email.delay` NIE zostało wywołane
        mock_send_confirmation_email.assert_not_called()
