from modeltranslation.translator import translator, TranslationOptions
from .models import BlogPost, BlogCategory, BlogTag

class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'seo_description', 'status')

class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class BlogTagTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(BlogPost, BlogPostTranslationOptions)
translator.register(BlogCategory, BlogCategoryTranslationOptions)
translator.register(BlogTag, BlogCategoryTranslationOptions)

