from backend.config.settings.base import *  # noqa
from backend import logger
SECRET_KEY = env("SECRET_KEY")
logger.debug(f"SECRET_KEY:------------------------------------ {SECRET_KEY}")
DEBUG = True
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=["*"])
# ADMIN SETTINGS
ADMIN_URL = env("ADMIN_URL")
ADMINS = [
    (env("ADMIN_NAME"), env("ADMIN_EMAIL")),
]

MANAGERS = ADMINS

# DATABASES SETTINGS
DATABASES = {
    "default":  {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("NAME"),
        "USER": env("USER"),
        "PASSWORD": env("PASSWORD"),
        "HOST": env("HOST"),
        "PORT": env("PORT"),
    }
}

# CACHES SETTINGS
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL SETTINGS
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")

# DEBUG TOOLBAR
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# DJANGO EXTENSIONS
INSTALLED_APPS += ["django_extensions"]

# CELERY SETTINGS
CELERY_TASK_EAGER_PROPAGATES = True
