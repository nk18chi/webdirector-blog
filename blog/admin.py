from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogTag, Image
from modeltranslation.admin import TranslationAdmin

class BlogPostAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'title_en', 'status', 'status_en', 'created_at',
                    'category')
    list_display_links = ('id',)

admin.site.register(BlogPost, BlogPostAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')

admin.site.register(Image, ImageAdmin)


class BlogCategoryAdmin(TranslationAdmin):
# class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_en', 'order')
    list_display_links = ('id',)

admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogTagAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'name_en')
    list_display_links = ('id',)

admin.site.register(BlogTag, BlogTagAdmin)