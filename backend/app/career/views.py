from rest_framework.generics import ListAPIView
from .models import Opportunity, Info
from .serializers import OpportunitySerializer, InfoSerializer

class OpportunityListAPIView(ListAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


class JobTypeListAPIView(ListAPIView):
    serializer_class = OpportunitySerializer

    def get_queryset(self):
        job_type = self.kwargs['job_type']
        return Opportunity.objects.filter(job_type=job_type)
    

class InfoListAPIView(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoTypeListAPIView(ListAPIView):
    serializer_class = InfoSerializer

    def get_queryset(self):
        info_type = self.kwargs['info_type']
        return Info.objects.filter(info_type=info_type)
