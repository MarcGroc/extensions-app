from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from users.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(GenericViewSet):
    """
    Test API endpoint .
    """

    queryset = User.objects.all()  # n+1
    serializer_class = UserSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user)
