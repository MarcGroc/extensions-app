"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""


from django.core.asgi import get_asgi_application

from config.helper_functions import settings_loader
from config.websocket import websocket_application

settings_loader()

django_application = get_asgi_application()


async def application(scope, receive, send) -> None:
    if scope["type"] == "http":
        await django_application(scope, receive, send)
    elif scope["type"] == "websocket":
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
