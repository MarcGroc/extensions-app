from django.contrib import admin

from payment.models import StripePaymentLink, StripePrice, StripeProduct
from payment.stripe_service import StripeService


@admin.register(StripeProduct)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["stripe_product_id", "created_at", "updated_at"]
    list_display = ["name", "description", "active", "default_price", "created_at", "updated_at"]

    def save_model(self, request, obj, form, change):
        if not obj.stripe_product_id:
            stripe_product = StripeService.create_product(obj.name, obj.description, obj.active)
            obj.stripe_product_id = stripe_product.id
        else:
            StripeService.update_product(
                obj.stripe_product_id,
                name=obj.name,
                description=obj.description,
                active=obj.active,
                default_price=obj.default_price * 100,
            )
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.stripe_product_id:
            StripeService.delete_product(obj.stripe_product_id)
        super().delete_model(request, obj)


@admin.register(StripePrice)
class StripePriceAdmin(admin.ModelAdmin):
    readonly_fields = ["stripe_price_id", "created_at", "updated_at"]
    list_display = ["nickname", "currency", "unit_amount", "product", "active", "created_at", "updated_at"]

    def save_model(self, request, obj, form, change):
        if not obj.stripe_price_id:
            stripe_price = StripeService.create_price(obj.currency, obj.unit_amount, obj.product.stripe_product_id)
            obj.stripe_price_id = stripe_price.id
        else:
            StripeService.update_price(obj.stripe_price_id, active=obj.active, nickname=obj.nickname)
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.stripe_price_id:
            StripeService.update_price(obj.stripe_price_id, active=False)
        super().delete_model(request, obj)


@admin.register(StripePaymentLink)
class StripePaymentLinkAdmin(admin.ModelAdmin):
    readonly_fields = ["stripe_payment_link_url", "stripe_payment_link_id", "created_at", "updated_at"]
    list_display = ["stripe_payment_link_url", "stripe_payment_link_id", "active", "created_at", "updated_at"]

    def save_model(self, request, obj, form, change):
        if not obj.stripe_payment_link_id:
            stripe_payment_link = StripeService.create_payment_link(
                obj.price.stripe_price_id,
                "redirect/to/user-dashboard",  # TODO: change url
            )
            obj.stripe_payment_link_id = stripe_payment_link.id
            obj.stripe_payment_link_url = stripe_payment_link.url
        else:
            StripeService.update_payment_link(obj.stripe_payment_link_id, metadata={"active": obj.active})
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.stripe_payment_link_id:
            StripeService.update_payment_link(obj.stripe_payment_link_id, metadata={"active": False})
        super().delete_model(request, obj)
