from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_prometheus.models import ExportModelOperationsMixin


class User(ExportModelOperationsMixin("user"), AbstractUser):
    first_name = models.CharField(_("First Name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    tier = models.CharField(
        choices=[("free", "free"), ("basic", "basic"), ("pro", "pro")], max_length=5, default="free"
    )

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.pk})
