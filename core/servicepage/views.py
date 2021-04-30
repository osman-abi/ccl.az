from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Service
# Create your views here.



class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'services/service_template.html'