from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_prometheus.models import ExportModelOperationsMixin


class User(ExportModelOperationsMixin("user"), AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=50)
    first_name = CharField(_("First Name"), max_length=50)
    last_name = CharField(_("Last Name"), max_length=50)

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.name})
