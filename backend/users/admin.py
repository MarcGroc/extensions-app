from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import admin as auth_admin

from config.settings.base import LOGIN_URL
from users.models import User

admin.site.login = staff_member_required(admin.site.login, login_url=LOGIN_URL)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    readonly_fields = [
        "stripe_customer_id",
        "date_joined",
        "last_login",
        "updated_at",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_display = ["username", "balance", "is_superuser", "updated_at", "is_active", "date_joined", "last_login"]
    search_fields = ["username", "email", "first_name", "last_name", "balance"]
    ordering = ["balance"]
