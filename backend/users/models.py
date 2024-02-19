from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse


class User(AbstractUser):
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)
    username = CharField(max_length=150, unique=True)

    def get_absolut_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
