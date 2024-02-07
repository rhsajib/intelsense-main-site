from django.urls import path
from .views import InvitationListAPIView, InvitationDetailAPIView, InvestorListAPIView, InvestorDetailAPIView


app_name = 'investors'


urlpatterns = [
    path('invitations/', InvitationListAPIView.as_view(), name='invitation-list'),
    path('invitations/<uuid:id>/', InvitationDetailAPIView.as_view(), name='invitation-detail'),
    path('', InvestorListAPIView.as_view(), name='investor-list'),
    path('<uuid:id>/', InvestorDetailAPIView.as_view(), name='investor-detail'),
]
