from django.contrib import admin
from .models import Like, Post, Profile, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)