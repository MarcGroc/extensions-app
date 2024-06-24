from django.urls import path

from payment.views import stripe_webhook

urlpatterns = [
    path("stripe/webhook/", stripe_webhook, view_name="stripe-webhook"),
]
