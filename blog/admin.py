from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogTag, Image
from modeltranslation.admin import TranslationAdmin

class BlogPostAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'status', 'created_at',
                    'category')
    list_display_links = ('id', 'title')

admin.site.register(BlogPost, BlogPostAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')

admin.site.register(Image, ImageAdmin)


class BlogCategoryAdmin(TranslationAdmin):
# class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    list_display_links = ('id', 'name')

admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogTagAdmin(TranslationAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(BlogTag, BlogTagAdmin)