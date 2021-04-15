from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    return HttpResponse('<p> test </p>')