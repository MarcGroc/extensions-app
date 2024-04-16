"""
URL configuration for config project.
"""
from config.settings.development import ADMIN_URL
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from users.api.views import ExampleTextView

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("prometheus/", include("django_prometheus.urls")),
    path("accounts/", include("allauth.urls")),
    path(ADMIN_URL, admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    path("api/", include(("config.api_router", "api"), namespace="api")),
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("example/", ExampleTextView.as_view(), name="example"),  # example url for vue te
]
