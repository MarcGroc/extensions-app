"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application

from config.load_settings import loader_settings

loader_settings()

application = get_wsgi_application()
