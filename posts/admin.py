from django.contrib import admin
from .models import Post, ViewCounter


admin.site.register(Post)
admin.site.register(ViewCounter)
