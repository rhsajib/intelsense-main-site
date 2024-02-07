from rest_framework.generics import ListAPIView, CreateAPIView
from .models import CustomerContact
from .serializers import CustomerContactSerializer

class CustomerContactListAPIView(ListAPIView):
    queryset = CustomerContact.objects.all()
    serializer_class = CustomerContactSerializer

class CustomerContactCreateAPIView(CreateAPIView):
    queryset = CustomerContact.objects.all()
    serializer_class = CustomerContactSerializer
