from rest_framework import serializers
from .models import CustomerContact

class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContact
        fields = '__all__'
