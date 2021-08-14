from rest_framework import serializers
from papers.models import ResearchPaper

class SerializeResearchPaper(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'author', 'topic', 'summary')
        model = ResearchPaper
