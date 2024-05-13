from rest_framework import serializers

from contact.models import Newsletter, Question


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["name", "email", "message"]


class ComingSoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["name", "email"]
