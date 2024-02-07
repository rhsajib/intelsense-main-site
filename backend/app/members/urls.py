from django.urls import path
from .views import MemberListAPIView, MemberDetailAPIView, TeamListAPIView, MemberListByTeamAPIView

app_name = 'members'


urlpatterns = [
    path('', MemberListAPIView.as_view(), name='member-list'),
    path('<uuid:id>/', MemberDetailAPIView.as_view(), name='member-detail'),
    path('teams/', TeamListAPIView.as_view(), name='team-list'),
    path('by_team/<str:team>/', MemberListByTeamAPIView.as_view(), name='member-list-by-team'),
]
