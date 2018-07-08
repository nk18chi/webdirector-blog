from django.db import models

class Idea(models.Model):
    text = models.CharField(max_length=225, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1, choices=[(0, '非公開'), (1, '公開中')])

    def __repr__(self):
        return "{}: {}".format(self.pk, self.text)

    __str__ = __repr__
