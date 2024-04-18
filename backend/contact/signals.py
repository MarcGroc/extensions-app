from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Question
from .tasks import send_confirmation_email


@receiver(post_save, sender=Question)
def send_confirmation(sender, instance, created, **kwargs):
    if created and not instance.confirmation_sent:
        send_confirmation_email.delay(instance.id)
