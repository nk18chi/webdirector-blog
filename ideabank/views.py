# coding: utf-8

import django_filters
from rest_framework import viewsets, filters
from .models import Idea
from .serializer import IdeaSerializer
from random import sample

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.filter(
        status__exact=1,
    ).order_by('?')[:3]
    serializer_class = IdeaSerializer
