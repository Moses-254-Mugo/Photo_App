from django.contrib import admin
from .models import Profile, Images, Comments, Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(Images)
admin.site.register(Comments)
admin.site.register(Follow)