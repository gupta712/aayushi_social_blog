from django.db import models
from django.contrib.auth.models import User


class SocialMedia(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/')
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    slug  = models.SlugField(blank=True, unique=True)
    video_file = models.FileField(upload_to='post_files',blank=True,null=True)
