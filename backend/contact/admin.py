from contact.models import Question
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Question)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("email", "message")
    fields = ("name", "email", "message")
    search_fields = ["name", "email", "message"]

    def reply(self, obj):
        url = reverse("contact:reply", kwargs={"id": obj.id})
        return format_html('<a href="{}">Reply</a>', url)

    reply.short_description = "Reply"
    list_display = ("name", "email", "message", "reply")
