from django.contrib import admin

from book import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'published', 'rubric', 'author']


@admin.register(models.Rubric)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']