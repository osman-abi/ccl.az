from django.urls import path
from .views import  BlogDetailView, blogs
from django.views.generic import TemplateView

urlpatterns = [
    path('', blogs, name='blogs'),
    path('<int:pk>/', BlogDetailView.as_view(),name='blog_detail')
]
