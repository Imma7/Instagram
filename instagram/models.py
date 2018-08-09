from django.db import models
from django.contrib.auth.models import User
import datetime as dt 
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
      
# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', blank=True)
    bio = models.TextField(max_length=50, blank=True, null=True)
    # username = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile') 

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

    @classmethod
    def get_by_id(cls,id):
        profile=Profile.objects.filter(user=id)
        return profile

    @classmethod
    def search_by_username(cls, search_term):
        profiles = cls.objects.filter(bio__icontains=search_term)
        return profiles

    

    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length = 30)
    image_caption = models.CharField(max_length = 30, blank = True, null=True)
    comments = models.TextField()
    likes = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posted_by", null = True)
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

    @classmethod
    def get_profile_images(cls,profile):
        images = Image.objects.filter(profile_pk=profile)
        return images

    def __str__(self):
        return self.image_name

class Likes(models.Model):
    postid = models.IntegerField()
    liker = models.CharField(max_length = 20)
    
