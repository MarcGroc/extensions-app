from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from contact.api.views import ComingSoonViewSet, ContactViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"contact", ContactViewSet, basename="contact")
router.register(r"coming-soon", ComingSoonViewSet, basename="coming-soon")

app_name = "api"
urlpatterns = router.urls
