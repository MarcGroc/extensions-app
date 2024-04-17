from contact.api.views import ContactViewSet
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"users", UserViewSet, basename="users")

router.register(r"contact", ContactViewSet, basename="contact")


app_name = "api"
urlpatterns = router.urls
