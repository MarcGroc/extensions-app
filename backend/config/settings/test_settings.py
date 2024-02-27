from .base import *  # noqa

env.read_env(str(BASE_DIR / ".env/.env.dev"))
SECRET_KEY = "test"
ALLOWED_HOSTS = ["*"]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("NAME"),
        "USER": env("USER"),
        "PASSWORD": env("PASSWORD"),
        "HOST": env("HOST"),
        "PORT": env("PORT"),
    }
}

AXES_ENABLED = False  # switch for axes testing
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
