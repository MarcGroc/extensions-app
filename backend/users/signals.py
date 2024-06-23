from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Group
from django.dispatch import receiver
from loguru import logger

from .tasks import create_stripe_customer, send_welcome_email


@receiver(user_signed_up)
def signal_send_welcome_email(request, user, created, **kwargs) -> None:
    if created:
        send_welcome_email.delay(user.id)
        logger.success(f"Welcome email sent to {user.id}")


@receiver(user_signed_up)
def signal_create_stripe_customer(sender, instance, created, **kwargs) -> None:
    if created:
        create_stripe_customer.delay(instance.id)
        logger.success(f"Stripe customer created for {instance.id}")


@receiver(user_signed_up)
def add_user_to_group(sender, instance, created, **kwargs) -> None:
    if created:
        group = Group.objects.get(name="Users")
        instance.groups.add(group)
        logger.success(f"User {instance.id} added to group {group.name}")
