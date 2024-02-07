from django.urls import path
from .views import OpportunityListAPIView, InfoListAPIView, JobTypeListAPIView, InfoTypeListAPIView

app_name = 'career'

urlpatterns = [
    path('opportunities/', OpportunityListAPIView.as_view(), name='opportunity-list'),
    path('info/', InfoListAPIView.as_view(), name='info-list'),
    path('jobs/<str:job_type>/', JobTypeListAPIView.as_view(), name='job-list'),
    path('info/<str:info_type>/', InfoTypeListAPIView.as_view(), name='info-type-list'),
]
