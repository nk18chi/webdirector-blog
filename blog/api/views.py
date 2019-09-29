from rest_framework import viewsets

from .serializers import BlogPostSerializer
from blog.models import BlogPost


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
