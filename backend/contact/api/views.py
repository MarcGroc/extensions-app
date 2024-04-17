from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import ContactSerializer


class ContactViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
