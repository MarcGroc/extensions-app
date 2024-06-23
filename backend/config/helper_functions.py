import os

import environ

env = environ.Env()
env.read_env("../.env")


def settings_loader() -> None:
    if env("DEBUG") == "True":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
