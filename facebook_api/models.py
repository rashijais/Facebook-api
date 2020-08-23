from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic=models.ImageField(upload_to='profile_images',blank=True)
    def __str__(self):
        return self.username

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(max_length=500, blank=True,null=True)
    image=models.ImageField(upload_to='images',blank=True)
    files=models.FileField(upload_to='file',blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s"%(self.title)

    class Meta:
        ordering = ['-date_created']
