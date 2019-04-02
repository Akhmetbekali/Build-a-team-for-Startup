from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    contact = models.CharField(max_length=20, default='')
    speciality = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='profile_image', blank=True)


class ProjectPage(models.Model):
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    # image = models.ImageField()

    type = models.CharField(max_length=20, default='project')
    title = models.CharField(max_length=30, default='New Project')
    description = models.CharField(max_length=500, default='')


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


def __str__(self):
    return f'{self.user.username} UserProfile'


def save(self):
    super().save()

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)
