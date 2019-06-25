from django.contrib import admin

# Register your models here.
from .models import PetPost


class PetsPost(admin.ModelAdmin):
    list_display = ['pet', 'post_title', 'monetization', 'post_type', 'funding_goal']
    list_display_links = ['pet', 'post_title', 'monetization', 'post_type', 'funding_goal']
    list_per_page = 25


admin.site.register(PetPost, PetsPost)