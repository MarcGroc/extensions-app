"""
Base setting to use in other settings files.
"""

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()

# Check if  production or development and read .env
# IS_PRODUCTION = env.bool("IS_PRODUCTION", default=False)
# if IS_PRODUCTION:
env.read_env(str(BASE_DIR / ".env/.env.dev"))
# env.read_env(str(BASE_DIR / ".env/.env.dev"))

# GENERAL SETTINGS

# On Windows must set to system timezone
TIME_ZONE = "UTC"
USE_TZ = True

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
USE_I18N = True
LOCALE_PATHS = [str(BASE_DIR / "locale")]

SITE_ID = 1
# APPS
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",  # noqa
    "django_celery_beat",
    "corsheaders",  # noqa
    "drf_spectacular",
    "axes",
]
LOCAL_APPS = [
    "backend.users",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# DATABASE SETTINGS

# DEFAULT AUTO FIELD used for models without primary key, if switched it will update primary keys!
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# MIGRATIONS


# URLS SETTINGS
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# AUTHENTICATION SETTINGS
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesStandaloneBackend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# Can be set only once during first migration
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "login"

# Password validation, prevents users from using "weak" passwords
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
# PASSWORD HASHING
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]


# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "axes.middleware.AxesMiddleware",
]


# STATIC
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATIC_URL = "/static/"


# MEDIA
MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"

# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# FIXTURES
FIXTURE_DIRS = (str(BASE_DIR / "fixtures"),)

# EMAIL SETTINGS
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_TIMEOUT = 5

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "debug_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "errors.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        # 'django.': {
        #     'handlers': ['file', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        "django.request": {
            "handlers": ["error_file", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        # 'backend': {
        #     'handlers': ['file', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}

# CELERY SETTINGS
CELERY_TIMEZONE = TIME_ZONE

CELERY_RESULT_EXTENDED = True
# Retry if failed
CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
# Task time limit, set to desired value in seconds
CELERY_TASK_TIME_LIMIT = 60
CELERY_TASK_SOFT_TIME_LIMIT = 60

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# Enable worker send task events to monitoring
CELERY_WORKER_SEND_TASK_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True

# ALLAUTH SETTINGS
ACCOUNT_ALLOW_REGISTRATION = env.bool("ALLOW_REGISTRATION", True)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# DRF SETTINGS
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
# CORS SETTINGS
# Restricts url for api
CORS_URLS_REGEX = r"^/api/.*$"

SPECTACULAR_SETTINGS = {
    "TITLE": "django-cutter API",
    "DESCRIPTION": "Documentation of API endpoints of django-cutter",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
}
