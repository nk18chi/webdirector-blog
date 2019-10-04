import os
from datetime import datetime
from django.db import models
from django.conf import settings
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BlogTag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField()
    created_at = models.DateTimeField(editable=False, default=datetime.now)
    updated_at = models.DateTimeField(editable=False, default=datetime.now)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownxField('本文', help_text='Markdown形式で書いてください。')
    seo_description = models.TextField()
    status = models.IntegerField(default=0, choices=[(0, '下書き'), (1, '公開')])
    created_at = models.DateTimeField(editable=True, default=datetime.now)
    updated_at = models.DateTimeField(editable=False, default=datetime.now)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    image_square = models.ForeignKey(Image, on_delete=models.CASCADE)
    blog_tag = models.ManyToManyField(BlogTag)

    def __str__(self):
        return self.title

    def text_to_markdown(self):
        return markdownify(self.content)
