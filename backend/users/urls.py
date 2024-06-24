from django.urls import path

from users.api.views import UserViewSet

# from users.views import RedirectView

app_name = "users"
urlpatterns = [
    # path("<str:username>/", UserDetailView.as_view(), name="detail"),
    # path("redirect/", RedirectView.as_view(), name="redirect"),
    path("api/user/", UserViewSet.as_view(), name="api-user"),
]
