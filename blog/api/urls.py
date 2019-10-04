from rest_framework import routers

from .views import BlogPostViewSet

blogpost_router = routers.DefaultRouter()
blogpost_router.register(r'', BlogPostViewSet)
