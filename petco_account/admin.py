from django.contrib import admin

# Register your models here.
from .models import Profile


class Account(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']
    list_per_page = 25


admin.site.register(Profile, Account)