from django.contrib import admin
from.models import SocialMedia
from django.contrib.auth.models import User
# Register your models here.
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['user','image','title','body','slug']
admin.site.register(SocialMedia,SocialMediaAdmin)
