from django.shortcuts import render
from django.views.generic import ListView
from .models import About
# Create your views here.

class AboutPage(ListView):
    model = About
    context_object_name = 'abouts'
    template_name = 'about/index.html'
