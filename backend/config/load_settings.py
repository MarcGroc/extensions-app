import os

import environ

env = environ.Env()
env.read_env("../.env")


def loader_settings():
    if env("DEBUG") == "True":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
