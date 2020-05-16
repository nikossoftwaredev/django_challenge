from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializers

#generate a CRUD environment
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializers #specifying the serialize class we just made