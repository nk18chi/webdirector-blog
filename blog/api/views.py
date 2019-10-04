from rest_framework import viewsets

from .serializers import BlogPostSerializer
from blog.models import BlogPost


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        queryset = BlogPost.objects.filter(
            status__exact=1
        ).order_by('-created_at')
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')

        if category:
            queryset = queryset.filter(category_id=category)
        elif tag:
            queryset = queryset.filter(blog_tag=tag)

        return queryset
