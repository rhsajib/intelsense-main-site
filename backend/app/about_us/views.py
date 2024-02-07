from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import AboutUs, Statement, Timeline
from .serializers import AboutUsSerializer, StatementSerializer, TimelineSerializer

class AboutUsListAPIView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsDetailByTopicAPIView(RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    lookup_field = 'topic'

class StatementListAPIView(ListAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class TimelineListAPIView(ListAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

class TimelineDetailByYearAPIView(RetrieveAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    lookup_field = 'year'
