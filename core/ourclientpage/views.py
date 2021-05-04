from django.shortcuts import render
from .models import OurCLients, PageImage
# Create your views here.



def client_list(request):
    clients = OurCLients.objects.all()
    images = PageImage.objects.all()
    return render(request, 'about/our-clients.html', {"clients":clients,"images":images})

    
