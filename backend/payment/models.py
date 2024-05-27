from django.db import models

from users.models import User


class StripeProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    default_price = models.IntegerField()
    stripe_product_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class StripePayment(models.Model):
    stripe_payment_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    customer_email = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.stripe_payment_id


class StripePrice(models.Model):
    stripe_price_id = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(max_length=3)
    unit_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(StripeProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.stripe_price_id
