from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView,DetailView
# Create your views here.

def blogs(request):
    blog = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog, 10)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'news/index.html',{'pages':pages} )
        

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'news/news_template.html'

