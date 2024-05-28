import stripe
from loguru import logger


def handle_stripe_errors_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except stripe.error.CardError as e:
            logger.error(f"Card error: {e.user_message}")
            logger.error(f"Status is: {e.http_status}")
            logger.error(f"Code is: {e.code}")
            logger.error(f"Param is: {e.param}")
        except stripe.error.RateLimitError as e:
            logger.error("Too many requests made to the API too quickly")
            logger.error(e)
        except stripe.error.InvalidRequestError as e:
            logger.error("Invalid parameters were supplied to Stripe's API")
            logger.error(e)
        except stripe.error.AuthenticationError as e:
            logger.error("Authentication with Stripe's API failed")
            logger.error(e)
        except stripe.error.APIConnectionError as e:
            logger.error("Network communication with Stripe failed")
            logger.error(e)
        except stripe.error.StripeError as e:
            logger.error("Display a very generic error to the user, and maybe send yourself an email")
            logger.error(e)

        except Exception as e:
            logger.error("Something else happened, completely unrelated to Stripe")
            logger.error(f"Unexpected error: {e}")

    return wrapper
