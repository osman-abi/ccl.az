from django.contrib import admin
from .models import ContactInfo,ContactUs,Facebook,ChooseUs, LinkedIn, Instagram, Whatsapp, SubscribedUsers
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(ContactInfo)
admin.site.register(Facebook)
admin.site.register(ChooseUs)
admin.site.register(Instagram)
admin.site.register(LinkedIn)
admin.site.register(Whatsapp)
admin.site.register(SubscribedUsers)