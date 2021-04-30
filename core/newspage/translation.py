from .models import Blog
from modeltranslation.translator import register, TranslationOptions

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('blog_title', 'blog_description', 'blog_context')
    
