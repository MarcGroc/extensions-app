from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
