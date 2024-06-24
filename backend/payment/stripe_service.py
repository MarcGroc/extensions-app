import stripe
from django.conf import settings
from loguru import logger

from payment.error_handler import handle_stripe_errors_decorator

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeService:
    @staticmethod
    @handle_stripe_errors_decorator
    def create_product(name, description, active):
        product = stripe.Product.create(name=name, description=description, active=active)
        logger.success(f"Product {name} created with ID {product.id}")
        return product

    @staticmethod
    @handle_stripe_errors_decorator
    def update_product(product_id, **kwargs):
        product = stripe.Product.modify(product_id, **kwargs)
        logger.success(f"Product updated with ID {product_id}")
        return product

    @staticmethod
    @handle_stripe_errors_decorator
    def delete_product(product_id):
        stripe.Product.delete(product_id)
        logger.success(f"Product deleted with ID {product_id}")

    @staticmethod
    @handle_stripe_errors_decorator
    def create_price(currency, unit_amount, product_id):
        price = stripe.Price.create(currency=currency, unit_amount=unit_amount * 100, product=product_id)
        logger.success(f"Price created with ID {price.id}")
        return price

    @staticmethod
    @handle_stripe_errors_decorator
    def update_price(price_id, **kwargs):
        price = stripe.Price.modify(price_id, **kwargs)
        logger.success(f"Price updated with ID {price_id}")
        return price

    @staticmethod
    @handle_stripe_errors_decorator
    def create_payment_link(price_id, after_completion_url):
        payment_link = stripe.PaymentLink.create(
            line_items=[{"price": price_id, "quantity": 1}],
            after_completion={"type": "redirect", "url": after_completion_url},
        )
        logger.success(f"Payment link created with ID {payment_link.id}")
        return payment_link

    @staticmethod
    @handle_stripe_errors_decorator
    def update_payment_link(payment_link_id, **kwargs):
        payment_link = stripe.PaymentLink.modify(payment_link_id, **kwargs)
        logger.success(f"Payment link updated with ID {payment_link_id}")
        return payment_link
