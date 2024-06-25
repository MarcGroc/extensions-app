"""
Test settings.
"""

from .base import *  # noqa

#
# env = environ.Env()
# env.read_env(str(BASE_DIR / "../.env"))
SECRET_KEY = "test"
ALLOWED_HOSTS = ["*"]
DEBUG = True
PROJECT_NAME = "testing"
DOMAIN = "test"
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
STRIPE_SECRET_KEY = "jdsfj"
STRIPE_PUBLISHABLE_KEY = "shdfhud"
# STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_db",
        "USER": "test_user",
        "PASSWORD": "test_password",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

AXES_ENABLED = False  # switch for axes testing
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
