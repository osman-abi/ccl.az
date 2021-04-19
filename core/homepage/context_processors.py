from .models import Logo,Support

def logo(request):
    logo_info = Logo.objects.all()
    support_info = Support.objects.all()
    return {
        'logos': logo_info,
        'supports':support_info
    }