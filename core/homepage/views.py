from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
from servicepage.models import Service
from .models import Slide, Logo, Statistica
from ourclientpage.models import OurCLients
from contactpage.models import ChooseUs



# Create your views here.

def home_page(request):
    statistics = Statistica.objects.all()
    choose_us = ChooseUs.objects.all()
    slide = Slide.objects.all()
    service = Service.objects.all()
    client = OurCLients.objects.all()
    return render(request, 'home/index.html', {'slides':slide,'services':service,'clients':client,'statistics':statistics,'choose_us':choose_us})


def select_language(request):
    if request.method == 'POST':
        pass
