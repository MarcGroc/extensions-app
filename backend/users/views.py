# from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse
# from django.views.generic import RedirectView
#
# User = get_user_model()
#
#
# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False
#
#     def get_redirect_url(self) -> str:
#         return reverse("users:detail", kwargs={"username": self.request.user.username})
