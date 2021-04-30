from .models import OurCLients
from modeltranslation.translator import register, TranslationOptions

@register(OurCLients)
class ClientTranslationOptions(TranslationOptions):
    fields = ('client_title','client_description','client_context')