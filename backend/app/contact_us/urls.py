from django.urls import path
from .views import CustomerContactCreateAPIView, CustomerContactListAPIView

app_name = 'contact_us'

urlpatterns = [
    path('', CustomerContactListAPIView.as_view(), name='customer-contact-list'),
    path('create/', CustomerContactCreateAPIView.as_view(), name='customer-contact-create'),
]

