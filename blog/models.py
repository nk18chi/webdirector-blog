import os
from datetime import datetime
from django.db import models
from django.conf import settings


class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50)
    upload_time = models.DateTimeField(default=datetime.now)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    seo_description = models.TextField()
    status = models.IntegerField(default=1, choices=[(1, '下書き'), (2, '公開')])
    created = models.DateTimeField(editable=True, default=datetime.now)
    updated = models.DateTimeField(editable=False, default=datetime.now)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True)
    image_square = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BlogPostTag(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    tag = models.ForeignKey(BlogTag, on_delete=models.CASCADE)