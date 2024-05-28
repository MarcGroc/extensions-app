from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_prometheus.models import ExportModelOperationsMixin


class User(ExportModelOperationsMixin("user"), AbstractUser):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(default=0)

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
