from django.contrib import admin
from .models import ContactInfo,ContactUs,Facebook,ChooseUs
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(ContactInfo)
admin.site.register(Facebook)
admin.site.register(ChooseUs)