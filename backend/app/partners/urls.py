from django.urls import path
from .views import (
    OrganizationListAPIView, 
    OrganizationDetailAPIView,
    OpinionListAPIView,
    OpinionDetailAPIView,
    PartnerListAPIView,
)

app_name = 'partners'

urlpatterns = [
    path('', PartnerListAPIView.as_view(), name='partners'),
    path('organizations/', OrganizationListAPIView.as_view(), name='organizations'),
    path('organizations/<uuid:id>/', OrganizationDetailAPIView.as_view(), name='organization-detail'),
    path('opinions/', OpinionListAPIView.as_view(), name='opinions'),
    path('opinions/<uuid:id>/', OpinionDetailAPIView.as_view(), name='opinion-detail'),
]
