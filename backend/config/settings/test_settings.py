"""
Test settings.
"""
from .base import *  # noqa

env.read_env(str(BASE_DIR / "../.env"))
SECRET_KEY = "test"
ALLOWED_HOSTS = ["*"]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

AXES_ENABLED = False  # switch for axes testing
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
