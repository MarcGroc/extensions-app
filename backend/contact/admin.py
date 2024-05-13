from django.contrib import admin

from contact.models import Newsletter, Question


@admin.register(Question)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "email", "message", "confirmation_sent", "created_at")
    fields = ("name", "email", "message", "confirmation_sent", "created_at", "answered", "answer")
    search_fields = ["name", "email", "message"]
    list_display = ("name", "email", "message", "confirmation_sent", "answered", "created_at")
    actions = ["reply_to_question"]


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    fields = ("name", "email")
    search_fields = ["name", "email"]
    list_display = ("name", "email", "created_at")
