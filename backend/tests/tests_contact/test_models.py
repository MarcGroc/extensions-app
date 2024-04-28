from django.test import TestCase

from contact.models import Question


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
        self.assertEqual(self.question.__str__(), f" Pytanie {self.question.id}")
        # Test if fields are correct
        self.assertEqual(self.question.name, "Test")
        self.assertEqual(self.question.email, "tst@test.com")
        self.assertEqual(self.question.message, "Test message")
        self.assertTrue(self.question.confirmation_sent)
        self.assertFalse(self.question.answered)
        self.assertIsNone(self.question.answer)

    def test_answer_question(self):
        # Test if question is answered
        self.question.answer = "Test answer"
        self.question.answered = True
        self.question.save()
        # Test if fields are correct
        updated_question = Question.objects.get(id=self.question.id)
        self.assertEqual(updated_question.answer, "Test answer")
        self.assertTrue(updated_question.answered)
