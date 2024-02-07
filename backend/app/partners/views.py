from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Organization, Opinion, Partner
from .serializers import OpinionSerializer, OrganizationSerializer, PartnerSerializer

class OrganizationListAPIView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailAPIView(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'id'


class OpinionListAPIView(ListAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


class OpinionDetailAPIView(RetrieveAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    lookup_field = 'id'  


class PartnerListAPIView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer