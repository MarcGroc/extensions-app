from django.urls import path

from .api.views import UserViewSet
from .views import RedirectView

app_name = "users"
urlpatterns = [
    # path("<str:username>/", UserDetailView.as_view(), name="detail"),
    path("redirect/", RedirectView.as_view(), name="redirect"),
    path("api/user/", UserViewSet.as_view(), name="api-user"),
]
