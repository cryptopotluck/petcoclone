from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CreatePet(models.Model):
    owner = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    pet_name = models.CharField(blank=False, max_length=25)
    pet_bread = models.CharField(blank=True, max_length=25)
    type_of_pet = (('Dog', 'Dog'),
                   ('Cat', 'Cat'),
                   ('Reptile', 'Reptile'),
                   ('Aquatic', 'Aquatic'),
                   ('Rodent', 'Rodent'),
                   ('Outdoor', 'Outdoor'),
                   ('Exotic', 'Exotic'))
    pet_type = models.CharField(max_length=50, choices=type_of_pet, default='Dog')
    birthday = models.DateField(blank=True, default='1996-07-10')
    pet_profile_pic = models.ImageField(upload_to='dog/%Y/%m/%d/', default='profile/default/dog_default.jpeg',
                                        blank=True)
    about_pet = models.TextField(blank=True)




