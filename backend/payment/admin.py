import stripe
from django.conf import settings
from django.contrib import admin
from loguru import logger

from payment.error_handler import handle_stripe_errors_decorator

from .models import StripePaymentLink, StripePrice, StripeProduct

stripe.api_key = settings.STRIPE_SECRET_KEY


@admin.register(StripeProduct)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["stripe_product_id", "created_at", "updated_at"]
    list_display = ["name", "description", "active", "default_price", "created_at", "updated_at"]

    @handle_stripe_errors_decorator
    def save_model(self, request, obj, form, change):
        if not obj.stripe_product_id:
            stripe_product = stripe.Product.create(name=obj.name, description=obj.description, active=obj.active)
            obj.stripe_product_id = stripe_product.id
            logger.success(f"Product {obj.name} created with ID {stripe_product.id}")
        elif obj.stripe_product_id:
            stripe.Product.modify(
                obj.stripe_product_id,
                name=obj.name,
                description=obj.description,
                active=obj.active,
                default_price=obj.default_price * 100,
            )
            logger.success(f"Product {obj.name} updated with ID {obj.stripe_product_id}")
        super().save_model(request, obj, form, change)

    @handle_stripe_errors_decorator
    def delete_model(self, request, obj):
        if obj.stripe_product_id:
            stripe.Product.delete(obj.stripe_product_id)
            logger.success(f"Product {obj.name} deleted with ID {obj.stripe_product_id}")
        super().delete_model(request, obj)


@admin.register(StripePrice)
class StripePriceAdmin(admin.ModelAdmin):
    readonly_fields = ["stripe_price_id", "created_at", "updated_at"]
    list_display = ["nickname", "currency", "unit_amount", "product", "active", "created_at", "updated_at"]

    @handle_stripe_errors_decorator
    def save_model(self, request, obj, form, change):
        if not obj.stripe_price_id:
            stripe_price = stripe.Price.create(
                currency=obj.currency, unit_amount=obj.unit_amount * 100, product=obj.product.stripe_product_id
            )
            obj.stripe_price_id = stripe_price.id
            logger.success(f"Price for {obj.product.name} created with ID {stripe_price.id}")
        elif obj.stripe_price_id:
            stripe.Price.modify(obj.stripe_price_id, active=obj.active, nickname=obj.nickname)
            logger.success(f"Price for {obj.product.name} updated with ID {obj.stripe_price_id}")
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.stripe_price_id:
            stripe.Price.modify(
                obj.stripe_price_id,
                active=False,
            )
            logger.success(f"Price for {obj.product.name} archived with ID {obj.stripe_price_id}")
        super().delete_model(request, obj)


@admin.register(StripePaymentLink)
class StripePaymentLInkAdmin(admin.ModelAdmin):
    readonly_fields = ["stripe_payment_link_url", "stripe_payment_link_id", "created_at", "updated_at"]
    list_display = ["stripe_payment_link_url", "stripe_payment_link_id", "active", "created_at", "updated_at"]

    def save_model(self, request, obj, form, change):
        if not obj.stripe_payment_link_id:
            stripe_payment_link = stripe.PaymentLink.create(
                line_items=[
                    {
                        "price": obj.price.stripe_price_id,
                        "quantity": 1,
                    }
                ],
                after_completion={"type": "redirect", "url": "redirect/to/user-dashboard"},  # TODO: change url
            )
            obj.stripe_payment_link_id = stripe_payment_link.id
            obj.stripe_payment_link_url = stripe_payment_link.url
            logger.success(f"Payment link for {obj.product.name} created with ID {stripe_payment_link.id}")
        elif obj.stripe_payment_link_id:
            stripe.PaymentLink.modify(
                obj.stripe_payment_link_id,
                metadata={"active": obj.active},
            )
            logger.success(f"Payment link for {obj.product.name} updated with ID {obj.stripe_payment_link_id}")
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.stripe_payment_link_id:
            stripe.PaymentLink.modify(
                obj.stripe_payment_link_id,
                metadata={"active": False},
            )
            logger.success(f"Payment link for {obj.product.name} archived with ID {obj.stripe_payment_link_id}")
        super().delete_model(request, obj)
