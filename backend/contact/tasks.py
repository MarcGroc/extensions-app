from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from loguru import logger

from .models import Question

_email_content = {
    "intro": f"Witamy w {settings.PROJECT_NAME}!",
    "received": "Otrzymaliśmysmy twoją wiadomość. Odpowiemy jak najszybciej. :)",
    "thank_you": "Dziękujemy!",
}


@shared_task
def send_confirmation_email(question_id):
    question = Question.objects.get(id=question_id)
    subject = _email_content["intro"]
    message = f"{_email_content['received']}\n{_email_content['thank_you']}"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [question.email],
        fail_silently=False,
    )
    question.confirmation_sent = True
    question.save()

    logger.debug(f"Confirmation email sent to {question.email}")


# @shared_task
def reply_to_question(question: Question):
    question = Question.objects.get(id=question.id)
    subject = f"Odpowiedz na pytanie: {question.name}"
    message = question.answer
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        message,
        from_email,
        [question.email],
        fail_silently=False,
    )
