from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from .tasks import send_welcome_email


@receiver(user_signed_up)
def user_signed_up(request, user, **kwargs):
    send_welcome_email.delay(user.id)
