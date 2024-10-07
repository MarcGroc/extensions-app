from django.contrib import admin

from scraper.models import JobPosting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "link",
        "description",
        "budget",
        "hourly_range",
        "posted_on",
    )
    readonly_fields = [
        "title",
        "link",
        "description",
        "skills",
        "category",
        "budget",
        "hourly_range",
        "country",
        "posted_on",
        "guid",
        "created_at",
    ]
    ordering = ["-created_at"]
