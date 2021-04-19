from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import ContactUs, SubscribedUsers

# Create your views here.


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        subscribed_user = SubscribedUsers.objects.create(email=email)
        subscribed_user.save()
        return redirect('/')

    
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        message = request.POST.get('message', '')
        contact = ContactUs.objects.create(username=name, email=email, phone_number=phone_number, message=message)
        contact.save()
        return redirect('/')
    



