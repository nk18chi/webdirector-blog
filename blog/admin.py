from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogTag, Image
from markdownx.admin import MarkdownxModelAdmin


class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at',
                    'category')
    list_display_links = ('id', 'title')


admin.site.register(BlogPost, BlogPostAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')


admin.site.register(Image, ImageAdmin)


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    list_display_links = ('id', 'name')


admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(BlogTag, BlogTagAdmin)
