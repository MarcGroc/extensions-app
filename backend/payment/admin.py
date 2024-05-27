import stripe
from django.conf import settings
from django.contrib import admin
from loguru import logger

from payment.error_handler import handle_stripe_errors_decorator

from .models import StripePrice, StripeProduct

stripe.api_key = settings.STRIPE_SECRET_KEY


@admin.register(StripeProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "active", "default_price"]

    @handle_stripe_errors_decorator
    def save_model(self, request, obj, form, change):
        if not obj.stripe_product_id:
            stripe_product = stripe.Product.create(name=obj.name, description=obj.description, active=obj.active)
            obj.stripe_product_id = stripe_product.id
            logger.warning(f"Product {obj.name} created with ID {stripe_product.id}")
        elif obj.stripe_product_id:
            stripe.Product.modify(
                obj.stripe_product_id,
                name=obj.name,
                description=obj.description,
                active=obj.active,
                default_price=obj.default_price * 100,
            )
            logger.warning(f"Product {obj.name} updated with ID {obj.stripe_product_id}")
        super().save_model(request, obj, form, change)

    @handle_stripe_errors_decorator
    def delete_model(self, request, obj):
        if obj.stripe_product_id:
            stripe.Product.delete(obj.stripe_product_id)
            logger.warning(f"Product {obj.name} deleted with ID {obj.stripe_product_id}")
        super().delete_model(request, obj)


@admin.register(StripePrice)
class StripePriceAdmin(admin.ModelAdmin):
    list_display = ["stripe_price_id", "currency", "unit_amount", "created_at", "product"]

    @handle_stripe_errors_decorator
    def save_model(self, request, obj, form, change):
        if not obj.stripe_price_id:
            stripe_price = stripe.Price.create(
                currency=obj.currency, unit_amount=obj.unit_amount * 100, product=obj.product.stripe_product_id
            )
            obj.stripe_price_id = stripe_price.id
            logger.warning(f"Price for {obj.product.name} created with ID {stripe_price.id}")
        super().save_model(request, obj, form, change)
