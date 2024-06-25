import os

import environ

env = environ.Env()
env.read_env("../.env")


def settings_loader() -> None:
    # Skip loading settings during GitHub Actions tests
    if os.getenv("GITHUB_ACTIONS") == "true":
        return

    # Skip loading settings during tests
    if os.getenv("TESTING") == "true":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.test_settings")
        return
    if env("DEBUG") == "True":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
