from rest_framework import serializers

from blog.models import BlogPost, Image, BlogTag


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
    blog_tag = BlogTagSerializer(read_only=True, many=True)
    seo_description = serializers.SerializerMethodField()

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
