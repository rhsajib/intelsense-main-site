from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Invitation, Investor
from .serializers import InvitationSerializer, InvestorSerializer

class InvitationListAPIView(ListAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

class InvitationDetailAPIView(RetrieveAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    lookup_field = 'id'  # Specify the field to use for looking up the member

class InvestorListAPIView(ListAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class InvestorDetailAPIView(RetrieveAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    lookup_field = 'id'  # Specify the field to use for looking up the member