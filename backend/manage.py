#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys

from django.conf import settings
from loguru import logger

from config.helper_functions import settings_loader


def main():
    logger.info(f"Starting {settings.PROJECT_NAME} application...")
    settings_loader()
    if settings.DEBUG:
        logger.warning("APPLICATION IN DEVELOPMENT MODE")
    else:
        logger.warning("APPLICATION IN PRODUCTION MODE")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
