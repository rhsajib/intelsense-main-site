from django.urls import path
from .views import (
    AboutUsListAPIView, AboutUsDetailByTopicAPIView,
    StatementListAPIView, TimelineListAPIView, TimelineDetailByYearAPIView
)


app_name = 'about_us'


urlpatterns = [
    path('', AboutUsListAPIView.as_view(), name='aboutus-list'),
    path('<str:topic>/', AboutUsDetailByTopicAPIView.as_view(), name='aboutus-detail'),
    path('statements/', StatementListAPIView.as_view(), name='statement-list'),
    path('timeline/', TimelineListAPIView.as_view(), name='timeline-list'),
    path('timeline/<int:year>/', TimelineDetailByYearAPIView.as_view(), name='timeline-detail'),
]
