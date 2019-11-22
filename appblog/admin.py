from django.contrib import admin
from .models import Category, Tag, Post, Comment, PostAdmin


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)