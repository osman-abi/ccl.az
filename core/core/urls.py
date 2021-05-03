"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    path('selectlanguage/<str:lang_code>', views.set_language, name = 'select_language'),
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('haqqimizda/', include('aboutpage.urls')),
    path('contact/', include('contactpage.urls')),
    path('news/', include('newspage.urls')),
    path('services/', include('servicepage.urls')),
    path('clients/', include('ourclientpage.urls')),
    prefix_default_language=True,
)


urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
