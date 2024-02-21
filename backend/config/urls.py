"""
URL configuration for config project.
"""
from config.settings.development import ADMIN_URL
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path(ADMIN_URL, admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
]
