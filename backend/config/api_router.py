from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from contact.api.views import ComingSoonViewSet, ContactViewSet
from users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"users", UserViewSet, basename="users")

router.register(r"contact", ContactViewSet, basename="contact")
router.register(r"coming-soon", ComingSoonViewSet, basename="coming-soon")

app_name = "api"
urlpatterns = router.urls

# TODO: For early stage of development it stays as it is, not sure if i want to keep it in that way.
