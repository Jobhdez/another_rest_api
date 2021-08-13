from django.urls import path
from django.views.generic import TemplateView

app_name = 'papers'

urlpatterns = [
    path('', TemplateView.as_view(template_name="papers/index.html")),
    ]
