from django.urls import path
from .views import subscribe, contact_us
from django.views.generic import TemplateView

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('contact_us/', contact_us, name="contact_us"),
    path('', TemplateView.as_view(template_name='contact/index.html'), name='contact')
]
