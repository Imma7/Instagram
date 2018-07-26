from django.db import models
from django.contrib.auth.models import User
import datetime as dt 
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=30)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)

    def save_profile(self):
        return self.save()

    def update_profile(self):
        return self.update()

    def delete_profile(self):
        return self.delete()

    @classmethod
    def find_profile(search_profile, cls):
        profile = cls.objects.filter(username = search_profile)
        return profile

    def __str__(self):
        return self.username

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length = 30)
    image_caption = models.CharField(max_length = 30, blank = True, null=True)
    comments = HTMLField()
    likes = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete()

    def update_caption(self):
        return self.update()

    @classmethod
    def get_image_by_id(search_image, cls):
        image = cls.objects.filter(image_name = search_image)
        return image

    @classmethod
    def get_all(cls):
       images = cls.objects.order_by('-pub_date')
       return images

    def __str__(self):
        return self.image_name