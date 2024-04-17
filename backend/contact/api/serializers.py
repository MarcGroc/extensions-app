from contact.models import Question
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["name", "email", "message"]
