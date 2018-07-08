# coding: utf-8

from rest_framework import serializers
from .models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'text', 'created_at', 'status')
