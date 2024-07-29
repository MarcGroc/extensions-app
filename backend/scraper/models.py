from django.db import models


class JobPosting(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField()
    link = models.URLField(max_length=500)
    description = models.TextField()
    skills = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hourly_range = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    country = models.CharField()
    posted_on = models.DateTimeField(null=True, blank=True)
    guid = models.CharField(blank=True, null=True)
