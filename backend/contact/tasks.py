from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from loguru import logger

from .models import NewsletterSignup, Question

email_content = {
    "intro": f"Witamy w {settings.PROJECT_NAME}!",
    "received": "Otrzymaliśmysmy twoją wiadomość. Odpowiemy jak najszybciej. :)",
    "thank_you": "Dziękujemy!",
}


@shared_task
def send_confirmation_email(question_id: Question) -> None:
    question = Question.objects.get(id=question_id)
    subject = email_content["intro"]
    message = f"{email_content['received']}\n{email_content['thank_you']}"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [question.email],
        fail_silently=False,
    )
    question.confirmation_sent = True
    logger.info(f"Confirmation email sent to {question.id}")
    question.save()


@shared_task
def reply_to_question(question: Question) -> None:
    question = Question.objects.get(id=question)
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
    logger.info(f"Reply email sent to {question.id}")


@shared_task
def newsletter_signup(newsletter: NewsletterSignup) -> None:
    newsletter = NewsletterSignup.objects.get(id=newsletter)
    subject = email_content["intro"]
    message = f"{email_content['received']}\n{email_content['thank_you']}"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        message,
        from_email,
        [newsletter.email],
        fail_silently=False,
    )
    logger.info(f"Newsletter signup email sent to {newsletter.id}")
