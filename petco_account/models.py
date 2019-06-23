from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from create_dogs.models import CreatePet


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    about = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/%Y/%m/%d/', default='profile/default/Headshot-Placeholder-1.png',
                                      blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    pets = models.ManyToManyField(CreatePet, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
