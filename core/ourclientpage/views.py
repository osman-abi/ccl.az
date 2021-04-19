from django.shortcuts import render
from .models import OurCLients
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class ClientListView(ListView):
    model = OurCLients
    context_object_name = 'clients'
    template_name='about/our-clients.html'

# def client_list(request):
#     clients = OurCLients.objects.all()
#     page = request.GET.get('page', 1)
#       paginator = Paginator(clients, 10)
#        try:
#             pages = paginator.page(page)
#         except PageNotAnInteger:
#             pages = paginator.page(1)
#         except EmptyPage:
#             pages = paginator.page(paginator.num_pages)

    
