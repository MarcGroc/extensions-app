from .base import *  # noqa

env.read_env(str(BASE_DIR / ".env/.env.dev"))
DEBUG = True
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

# ADMIN SETTINGS
ADMIN_URL = "iaewrfhijxnx/"
ADMINS = [
    (env("ADMIN_NAME"), env("ADMIN_EMAIL")),
]

MANAGERS = ADMINS

# DATABASES SETTINGS
DATABASES = {
    "default": {
        "ENGINE": "django_prometheus.db.backends.postgresql",
        "NAME": env("NAME"),
        "USER": env("USER"),
        "PASSWORD": env("PASSWORD"),
        "HOST": env("HOST"),
        "PORT": env("PORT"),
    }
}
# Connection pool settings
CONNECTION_ATTEMPTS = 5
DELAY_BETWEEN_ATTEMPTS = 5


# CACHES SETTINGS
CACHES = {
    "default": {
        "BACKEND": "django_prometheus.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL SETTINGS
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")

# DEBUG TOOLBAR
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
# INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if DEBUG:
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]
# DJANGO EXTENSIONS
INSTALLED_APPS += ["django_extensions"]

# CELERY SETTINGS
CELERY_TASK_EAGER_PROPAGATES = True
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")


AXES_ENABLED = True
AXES_FAILURE_LIMIT = 3
AXES_COOLOFF_TIME = 0.1
AXES_ENABLE_ADMIN = True
AXES_VERBOSE = True

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",  # Allow Vue.js development server
]
