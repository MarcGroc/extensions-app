from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "contact"
    app_label = "contact"

    def ready(self) -> None:
        import contact.signals  # noqa
