from django.db import transaction
from loguru import logger
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from contact.models import NewsletterSignup, Question

from .serializers import ComingSoonSerializer, ContactSerializer


class ContactViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Question.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info("Contact request created")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ComingSoonViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ComingSoonSerializer
    queryset = NewsletterSignup.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info("Coming soon request created")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
