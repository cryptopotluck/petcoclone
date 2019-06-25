from django.db import models
from django.contrib.auth.models import User
from create_dogs.models import CreatePet
from django.urls import reverse
from petco_account.models import Profile
# Create your models here.


class PetPost(models.Model):
    pet = models.ForeignKey(CreatePet, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=30, blank=False)
    monetization_type = (('Funding', 'Funding'),
                         ('Non-Funding', 'Non-Funding'))
    monetization = models.CharField(max_length=50, choices=monetization_type, default='Non-Funding')
    type_of_post = (('Fun', 'Fun'),
                    ('Medical', 'Medical'),
                    ('In Memory of', 'In Memory of'),
                    ('Fundraiser', 'Fundraiser'),
                    ('Birthday', 'Birthday'))
    post_type = models.CharField(max_length=50, choices=type_of_post, default='Fun')
    post_body = models.TextField(blank=True)
    funding_goal = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, blank=True)
    funded_amount = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, blank=True)


    def get_absolute_url(self):
        return reverse('dog_post_detail', kwargs={'pk': self.pk})
