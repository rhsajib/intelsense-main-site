from django.urls import path
from .views import ServiceListAPIView, TopServiceListAPIView, ProvidedServiceListAPIView, ServiceDetailAPIView

app_name = 'services'

urlpatterns = [
    path('', ServiceListAPIView.as_view(), name='service-list'),
    path('<uuid:id>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('top/', TopServiceListAPIView.as_view(), name='top-service-list'),
    path('provided/', ProvidedServiceListAPIView.as_view(), name='provided-service'),
]
