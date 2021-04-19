from .models import Service

def service(request):
    return {
        'services':Service.objects.all()
    }