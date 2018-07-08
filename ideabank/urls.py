# coding: utf-8

from rest_framework import routers
from .views import IdeaViewSet

router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)
