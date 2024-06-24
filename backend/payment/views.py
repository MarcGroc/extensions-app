# import stripe
# from django.conf import settings
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# from payment.stripe_service import StripeService


# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
#     event = None
#
#     try:
#         event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
#     except ValueError:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError:
#         # Invalid signature
#         return HttpResponse(status=400)
#
#     # Handle the event
#     # if event["type"] == "payment_intent.succeeded":
#     # payment_intent = event["data"]["object"]
#     # Handle successful payment
#     # TODO: Handle other events here
#
#     return HttpResponse(status=200)
