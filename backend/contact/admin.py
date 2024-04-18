from contact.models import Question
from django.contrib import admin

from .tasks import reply_to_question


@admin.register(Question)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "email", "message", "confirmation_sent", "created_at")
    fields = ("name", "email", "message", "confirmation_sent", "created_at", "answered", "answer")
    search_fields = ["name", "email", "message"]
    list_display = ("name", "email", "message", "confirmation_sent", "answered", "created_at")
    actions = ["reply_to_question"]

    def save_model(self, request, obj, form, change):
        if "answer" in form.changed_data:
            if obj.answer and not obj.answered:
                reply_to_question(obj)
                obj.answered = True
                obj.save()
                self.message_user(request, "Answer sent")
            else:
                self.message_user(request, "Answer already sent")
        super().save_model(request, obj, form, change)
