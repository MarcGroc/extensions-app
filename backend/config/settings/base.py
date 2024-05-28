"""
Base setting to use in other settings files.
"""

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
env = environ.Env()

env.read_env(str(BASE_DIR / ".env/.env.dev"))

# GENERAL SETTINGS
# On local Windows must set to system timezone
TIME_ZONE = "UTC"
USE_TZ = True
PROJECT_NAME = env("PROJECT_NAME")

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
PROJECT_APPS = [
    "users",
    "contact",
    "payment",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.instagram",
    "allauth.socialaccount.providers.twitter",
    "allauth.socialaccount.providers.github",
    "django_celery_beat",
    "corsheaders",
    "drf_spectacular",
    "axes",
    "loguru",
    "django_prometheus",
    "dj_rest_auth",
    "dj_rest_auth.registration",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# DATABASE SETTINGS
# Connection pool settings
CONNECTION_ATTEMPTS = 5
DELAY_BETWEEN_ATTEMPTS = 5

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
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"

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
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "axes.middleware.AxesMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
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
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "from@example.com"

# LOGGING SETTINGS
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "config.loguru_config.InterceptHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": True,
        },
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
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory" # not used, not tested
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_ALLOW_REGISTRATION = env.bool("ALLOW_REGISTRATION", True)
ACCOUNT_USERNAME_MIN_LENGTH = 3
# SOCIALACCOUNT_PROVIDERS = {
#     "github": {
#         # For each provider, you can choose whether or not the
#         # email address(es) retrieved from the provider are to be
#         # interpreted as verified.
#         "VERIFIED_EMAIL": True
#     },
#     "google": {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         "APPS": [
#             {
#                 "client_id": env("GOOGLE_OAUTH2_CLIENT_ID"),
#                 "secret": env("GOOGLE_OAUTH2_CLIENT_SECRET"),
#                 "key": ""
#             },
#         ],
#         # These are provider-specific settings that can only be
#         # listed here:
#         "SCOPE": [
#             "profile",
#             "email",
#         ],
#         "AUTH_PARAMS": {
#             "access_type": "online",
#         },
#     }
# }
# DRF SETTINGS

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),  # disabled for testing
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# REST_AUTH


# CORS SETTINGS
CORS_ALLOW_ALL_ORIGINS = True
# Restricts url for api
# CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]

CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

SPECTACULAR_SETTINGS = {
    "TITLE": f"{env('PROJECT_NAME')} API",
    "DESCRIPTION": f"Documentation of API endpoints of {env('PROJECT_NAME')}",
    "VERSION": f"{env('PROJECT_VERSION')}",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
}

# PROMETHEUS SETTINGS
PROMETHEUS_LATENCY_BUCKETS = (
    0.01,
    0.025,
    0.05,
    0.075,
    0.1,
    0.25,
    0.5,
    0.75,
    1.0,
    2.5,
    5.0,
    7.5,
    10.0,
    25.0,
    50.0,
    75.0,
    float("inf"),
)
PROMETHEUS_EXPORT_MIGRATIONS = True

# AXES SETTINGS
AXES_ENABLED = True
AXES_FAILURE_LIMIT = 3  # number of failed logins, change if needed
AXES_COOLOFF_TIME = 0.1
AXES_ENABLE_ADMIN = True
AXES_VERBOSE = True

# STRIPE
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")
