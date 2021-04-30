from .models import About
from modeltranslation.translator import register, TranslationOptions

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('about_title', 'about_context',)
