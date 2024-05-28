import stripe
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from loguru import logger

from .models import User

stripe.api_key = settings.STRIPE_SECRET_KEY
# from django.contrib.auth import get_user_model
# from payment.error_handler import handle_stripe_errors_decorator
# User = get_user_model()

welcome_message = {
    "welcome": f"Witamy w {settings.PROJECT_NAME}!",
    "account_activation": "Kliknij link poniżej, aby aktywować konto.",
}

# User = get_user_model()


@shared_task
def send_welcome_email(user_id: User):
    user = User.objects.get(id=user_id)
    send_mail(
        welcome_message["welcome"],
        welcome_message["account_activation"],
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
    logger.info(f"Sent welcome email to {user.id}")


@shared_task
# @handle_stripe_errors_decorator
def create_stripe_customer(user_id: User):
    user = User.objects.get(id=user_id)
    if not user.stripe_customer_id:
        stripe_customer = stripe.Customer.create(name=user.name, email=user.email)
        user.stripe_customer_id = stripe_customer.id
        user.save()
