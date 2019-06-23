from django.contrib import admin

# Register your models here.
from .models import CreatePet


class Pets(admin.ModelAdmin):
    list_display = ['pet_name', 'pet_bread', 'pet_type']
    list_display_links = ['pet_name', 'pet_bread', 'pet_type']
    list_per_page = 25


admin.site.register(CreatePet, Pets)
