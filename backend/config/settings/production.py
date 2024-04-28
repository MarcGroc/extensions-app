"""
Production settings.
"""

from base import *  # noqa

DEBUG = False
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

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

# ADMIN
ADMIN_URL = env("ADMIN_URL")
ADMINS = [
    (env("ADMIN_NAME"), env("ADMIN_EMAIL")),
]
MANAGERS = ADMINS

# STORAGES
INSTALLED_APPS += ["storages"]
# AWS
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
AWS_QUERYSTRING_AUTH = False
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate",
}
AWS_S3_MAX_MEMORY_SIZE = env.int(
    "DJANGO_AWS_S3_MAX_MEMORY_SIZE",
    default=100_000_000,  # 100MB
)
AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STORAGES = {
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticStorage"},
    "static": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        "LOCATION": f"{aws_s3_domain}/static",
    },
    "media": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        "LOCATION": f"{aws_s3_domain}/media",
    },
}

STATIC_URL = f"https://{aws_s3_domain}/static/"
# MEDIA
MEDIA_URL = f"https://{aws_s3_domain}/media/"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# EMAIL
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="projectname <no-reply@localhost>",
)
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[projectname]")
