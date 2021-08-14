from django.urls import path
from .views import ResearchPaperList, ResearchPaperDetail

app_name = 'papers_api'

urlpatterns = [
    path('<int:pk>/', ResearchPaperDetail.as_view(), name='detailcreate'),
    path('', ResearchPaperList.as_view(), name='listcreate'),
    ]
