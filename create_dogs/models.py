from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    birthday = models.DateField(blank=True, default='1996-07-10', null=True)
    pet_profile_pic = models.ImageField(upload_to='dog/%Y/%m/%d/', default='profile/default/dog_default.jpeg',
                                        blank=True)
    about_pet = models.TextField(blank=True)


    def get_absolute_url(self):
        return reverse('edit_pet', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.pet_name}'





