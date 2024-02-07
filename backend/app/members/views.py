from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Member, Team
from .serializers import MemberSerializer, TeamSerializer

class MemberListAPIView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetailAPIView(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'  # Specify the field to use for looking up the member

class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class MemberListByTeamAPIView(ListAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        team = self.kwargs['team']  # Extract the team from URL kwargs
        return Member.objects.filter(team=team)
