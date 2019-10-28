from rest_framework import serializers

from blog.models import BlogPost, Image, BlogTag, BlogCategory

from datetime import datetime


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'name',
            'image',
        )


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = (
            'id',
            'name',
        )


class BlogPostSerializer(serializers.ModelSerializer):
    image_square = ImageSerializer(read_only=True)
    category = BlogCategorySerializer(read_only=True)
    blog_tag = BlogTagSerializer(read_only=True, many=True)
    seo_description = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = (
            'id',
            'title',
            'seo_description',
            'created_at',
            'category',
            'image_square',
            'blog_tag'
        )

    def get_seo_description(self, obj):
        return obj.seo_description[:140]

    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
