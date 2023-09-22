from django.contrib import admin
from .models import Profile, Post, Like

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username','Image']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','no_likes']
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass