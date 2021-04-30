from modeltranslation.translator import register, TranslationOptions
from .models import Logo, Slide, Support, Statistica

@register(Logo)
class LogoTranslationOptions(TranslationOptions):
    fields = ('context',)

@register(Slide)
class SlideTranslationOptions(TranslationOptions):
    fields = ('context', 'button_name')
    
@register(Support)
class SupportTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'context')

@register(Statistica)
class StatisticaTranslationOptions(TranslationOptions):
    fields = ('title',)