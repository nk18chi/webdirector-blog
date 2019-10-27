from modeltranslation.translator import translator, TranslationOptions
from .models import BlogPost

class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'status')

translator.register(BlogPost, BlogPostTranslationOptions)

