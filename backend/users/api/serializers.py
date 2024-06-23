from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "stripe_customer_id", "balance", "groups"]
        read_only_fields = ["id", "stripe_customer_id", "balance"]
