from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length = 30)
    image_caption = models.CharField(max_length = 30, blank = True)
    comments = models.TextField(max_length=50, blank=True)
    likes = models.IntegerField()
    profile = models.ForeignKey(Profile)

    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete()

    def update_caption(self):
        return self.update()

    @classmethod
    def get_image_by_id(search_image, cls):
        image = cls.objects.filter(name = search_image)
        return image


class Profile(models.Model):
    profile_photo = models.ImageField()
    bio = models.TextField(max_length=50, blank=True)
    username = models.CharField()
    user = models.ForeignKey(User, blank=True)

    def save_profile(self):
        return self.save