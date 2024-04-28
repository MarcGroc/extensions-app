from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(GenericViewSet):
    """
    Test API endpoint .
    """

    queryset = User.objects.all()  # n+1
    serializer_class = UserSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user)

    @action(detail=False)
    def get_user_data(self, request):
        serializer = self.get_serializer(request.user, context={"request": request})
        return Response(serializer.data)
