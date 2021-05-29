from django.contrib import admin
from .models import Post
#管理画面にpostというUIを作ってくださいという意味
admin.site.register(Post)
# Register your models here.

