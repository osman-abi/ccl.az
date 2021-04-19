from django.urls import path
from .views import  ServiceDetailView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='services/index.html'), name='services'),
    path('<int:id>', ServiceDetailView.as_view(),name='service_detail')
]
