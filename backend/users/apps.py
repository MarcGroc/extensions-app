from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        import users.signals  # noqa: F401

        # try:
        #     return call_command("check_db")
        # except Exception as e:
        #     logger.exception(e)
