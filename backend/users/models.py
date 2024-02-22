from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_prometheus.models import ExportModelOperationsMixin


class User(ExportModelOperationsMixin("user"), AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)

    def get_absolut_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
