from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length = 30)
    image_caption = models.CharField(max_length = 30, blank = True)
    comments = models.TextField(max_length=50, blank=True)
    likes = models.IntegerField()
    profile = models.ForeignKey(Profile)


class Profile(models.Model):
    profile_photo = models.ImageField()
    bio = models.TextField(max_length=50, blank=True)
    username = models.CharField()