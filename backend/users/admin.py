from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import admin as auth_admin, get_user_model

from config.settings.development import LOGIN_URL

User = get_user_model()

admin.site.login = staff_member_required(admin.site.login, login_url=LOGIN_URL)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ["username", "name", "is_superuser", "date_joined"]
    search_fields = ["name", "email"]
    ordering = ["username"]
