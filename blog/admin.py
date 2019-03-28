from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogTag, BlogPostTag, Image
from markdownx.admin import MarkdownxModelAdmin


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'upload_time')
    list_display_links = ('id', 'name')
admin.site.register(Image, ImageAdmin)


# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'status', 'created', 'category', 'image_square')
#     list_display_links = ('id', 'title')
# admin.site.register(BlogPost, BlogPostAdmin)


class BlogPostTagInline(admin.TabularInline):
    model = BlogPostTag
    extra = 3


class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('id', 'title', 'status', 'created', 'category', 'image_square')
    list_display_links = ('id', 'title')
    inlines = [BlogPostTagInline]
admin.site.register(BlogPost, BlogPostAdmin)


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    list_display_links = ('id', 'name')
admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
admin.site.register(BlogTag, BlogTagAdmin)


class BlogPostTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'tag')
    list_display_links = ('id', 'post', 'tag')
admin.site.register(BlogPostTag, BlogPostTagAdmin)
