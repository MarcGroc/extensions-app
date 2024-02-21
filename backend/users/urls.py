from django.urls import path

from .views import RedirectView, UserDetailView

app_name = "users"
urlpatterns = [
    path("<str:username>/", UserDetailView.as_view(), name="detail"),
    path("redirect/", RedirectView.as_view(), name="redirect"),
]
