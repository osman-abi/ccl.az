from .models import Service
from modeltranslation.translator import register, TranslationOptions

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title','service_description','context')
