from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Service, ProvidedService
from .serializers import ServiceSerializer, ProvidedServiceSerializer

class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id' 

class TopServiceListAPIView(ListAPIView):
    queryset = Service.objects.filter(service_rating='top')
    serializer_class = ServiceSerializer


class ProvidedServiceListAPIView(ListAPIView):
    queryset = ProvidedService.objects.all()
    serializer_class = ProvidedServiceSerializer