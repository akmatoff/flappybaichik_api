from .models import Record
from rest_framework import viewsets, permissions
from .serializers import RecordSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]