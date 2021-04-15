from django.contrib import admin
from .models import ContactInfo,ContactUs,Facebook
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(ContactInfo)
admin.site.register(Facebook)