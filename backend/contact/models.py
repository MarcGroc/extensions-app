from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmation_sent = models.BooleanField(default=False)
    answer = models.TextField(blank=True, null=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return f"Pytanie {self.id}"


class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    confirmation_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Newsletter {self.id}"
