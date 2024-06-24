"""
Production settings.
"""

from .base import *  # noqa

DEBUG = False
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = ["*"]

ADMIN_URL = env("ADMIN_URL")
ADMINS = [
    (env("ADMIN_NAME"), env("ADMIN_EMAIL")),
]
MANAGERS = ADMINS
DATABASES = {
    "default": {
        "ENGINE": "django_prometheus.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}
# DATABASES = {"default": env.db("DATABASE_URL")}
# logger.debug(env.db("DATABASE_URL"))
# DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        },
    }
}

# EMAIL SETTINGS
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_USE_SSL = env("EMAIL_USE_SSL")

# LOGGING SETTINGS
# Logging is handled by loguru backend/config/loguru_config.py
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "default": {
            "level": "INFO",
            "class": "config.loguru_config.InterceptHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# ALLAUTH SETTINGS
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # not used, not tested
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_ALLOW_REGISTRATION = env.bool("ALLOW_REGISTRATION")
ACCOUNT_USERNAME_MIN_LENGTH = 3

# DRF SETTINGS
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.TokenAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),  # disabled for testing
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
SPECTACULAR_SETTINGS = {
    "TITLE": f"{env('PROJECT_NAME')} API",
    "DESCRIPTION": f"Documentation of API endpoints of {env('PROJECT_NAME')}",
    "VERSION": f"{env('PROJECT_VERSION')}",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
}

# CORS SETTINGS
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS")
CORS_ALLOW_HEADERS = env.list("CORS_ALLOW_HEADERS")
CORS_ALLOW_METHODS = env.list("CORS_ALLOW_METHODS")

CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
# SECURITY
# Protects against clickjacking
X_FRAME_OPTIONS = "DENY"

# Redirects to https
SECURE_SSL_REDIRECT = True

# CSRF cookie can be sent only over HTTPS
CSRF_COOKIE_SECURE = True

# Session can be sent only over HTTPS
SESSION_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# STORAGES
# INSTALLED_APPS += ["storages"]
# # AWS
# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
# AWS_QUERYSTRING_AUTH = False
# _AWS_EXPIRY = 60 * 60 * 24 * 7
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate",
# }
# AWS_S3_MAX_MEMORY_SIZE = env.int(
#     "DJANGO_AWS_S3_MAX_MEMORY_SIZE",
#     default=100_000_000,  # 100MB
# )
# AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
# AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
# aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
#
# STORAGES = {
#     "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticStorage"},
#     "static": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#         "LOCATION": f"{aws_s3_domain}/static",
#     },
#     "media": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#         "LOCATION": f"{aws_s3_domain}/media",
#     },
# }
#
# STATIC_URL = f"https://{aws_s3_domain}/static/"
# # MEDIA
# MEDIA_URL = f"https://{aws_s3_domain}/media/"
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
#
# # EMAIL
# DEFAULT_FROM_EMAIL = env(
#     "DJANGO_DEFAULT_FROM_EMAIL",
#     default="projectname <no-reply@localhost>",
# )
# SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[projectname]")
