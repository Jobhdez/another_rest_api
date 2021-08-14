from rest_framework import generics
from papers.models import ResearchPaper
from .serializers import SerializeResearchPaper

class ResearchPaperList(generics.ListCreateAPIView):
    queryset = ResearchPaper.objects.all()
    serializer_class = SerializeResearchPaper

class ResearchPaperDetail(generics.RetrieveDestroyAPIView):
    queryset = ResearchPaper.objects.all()
    serializer_class = SerializeResearchPaper
    
