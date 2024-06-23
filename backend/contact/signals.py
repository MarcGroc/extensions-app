from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import NewsletterSignup, Question
from .tasks import newsletter_signup, send_confirmation_email


@receiver(post_save, sender=Question)
def send_confirmation(sender, instance, created, **kwargs) -> None:
    if created and not instance.confirmation_sent:
        send_confirmation_email.delay(instance.id)


@receiver(post_save, sender=NewsletterSignup)
def send_signup_email(sender, instance, created, **kwargs) -> None:
    if created:
        newsletter_signup.delay(instance.id)
