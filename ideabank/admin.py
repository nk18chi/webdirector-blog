from django.contrib import admin
from .models import Idea

@admin.register(Idea)
class Idea(admin.ModelAdmin):
    pass
