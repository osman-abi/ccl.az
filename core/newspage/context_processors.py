from .models import Blog

def news(request):
    return {
        'blogs':Blog.objects.all()
    }