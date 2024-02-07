from rest_framework import serializers
from .models import Service, ProvidedService

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProvidedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvidedService
        fields = '__all__'
