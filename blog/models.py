import os
from datetime import datetime
from django.db import models


def delete_previous_file(function):
    """不要となる古いファイルを削除する為のデコレータ実装.

    :param function: メイン関数
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        """Wrapper 関数.

        :param args: 任意の引数
        :param kwargs: 任意のキーワード引数
        :return: メイン関数実行結果
        """
        self = args[0]

        # 保存前のファイル名を取得
        result = Image.objects.filter(pk=self.pk)
        previous = result[0] if len(result) else None
        super(Image, self).save()

        # 関数実行
        result = function(*args, **kwargs)

        # 保存前のファイルがあったら削除
        if previous:
            os.remove(previous.image.name)
        return result
    return wrapper


class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Image(models.Model):
    @delete_previous_file
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Image, self).save()

    @delete_previous_file
    def delete(self, using=None, keep_parents=False):
        super(Image, self).delete()

    name = models.CharField(max_length=50)
    upload_time = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='blog/static/blog/img/contents/')

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    seo_description = models.TextField()
    status = models.IntegerField(default=1, choices=[(1, '下書き'), (2, '公開')])
    created = models.DateTimeField(editable=True, default=datetime.now)
    updated = models.DateTimeField(editable=False, default=datetime.now)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    image_square = models.ForeignKey(Image, on_delete=models.CASCADE)

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