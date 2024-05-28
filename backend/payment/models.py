from django.db import models


class StripeProduct(models.Model):
    stripe_product_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    default_price = models.IntegerField()

    def __str__(self):
        return self.name


class StripePrice(models.Model):
    CURRENCY_CHOICES = (
        ("pln", "pln"),
        ("usd", "usd"),
        ("eur", "eur"),
        ("gbp", "gbp"),
    )
    stripe_price_id = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3)
    unit_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(StripeProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}  {self.unit_amount} - {self.nickname}"


class StripePaymentLink(models.Model):
    stripe_payment_link_id = models.CharField(max_length=50, blank=True, null=True)
    stripe_payment_link_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    price = models.ForeignKey(StripePrice, on_delete=models.CASCADE)
    product = models.ForeignKey(StripeProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment link for {self.product.name} - {self.stripe_payment_link_url}"
