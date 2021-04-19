from .models import ContactInfo, Facebook, Instagram, LinkedIn, Whatsapp

def contact(request):
    contact_info = ContactInfo.objects.all()
    facebook = Facebook.objects.all()
    instagram = Instagram.objects.all()
    linkedin = LinkedIn.objects.all()
    whatsapp = Whatsapp.objects.all()
    return {
        'contacts': contact_info,
        'facebooks': facebook,
        'instagrams': instagram,
        'linkedins': linkedin,
        'whatsapps':whatsapp
    }