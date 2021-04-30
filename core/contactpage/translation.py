from modeltranslation.translator import register, TranslationOptions
from .models import  ChooseUs

@register(ChooseUs)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('context',)