from django.shortcuts import render, redirect, reverse
from .models import CreatePet
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from tinymce.widgets import TinyMCE
from .forms import CreatePetForm

# Create your views here.


class CreateDogPage(CreateView):
    model = CreatePet
    fields = ['pet_name', 'pet_bread', 'pet_type', 'birthday', 'pet_profile_pic', 'about_pet']

    def get_form(self, form_class=CreatePetForm):
        form = super(CreateDogPage, self).get_form(CreatePetForm)
        form.fields['about_pet'].widget = TinyMCE()
        return form

    def form_valid(self, form):
        # form.instance.owner = self.request.user
        # form.instance.save()
        instance = form.save(commit=False)
        instance.owner_id = self.request.user.id
        instance.save()
        response = super().form_valid(form)
        self.object.save()
        return response

    def get_success_url(self):
        return reverse('update')

    def form_invalid(self,form):
        errors = form.errors
        for error in errors:
            print(error)



def dog_detail(requests):
    return render(requests, 'create_dogs/create_dog_detail.html')

def dog_edit_page(requests):
    return render(requests, 'create_dogs/create_dog_form_edit.html')

def dog_heaven(requests):
    return render(requests, 'create_dogs/dog_heaven.html')

def deleate_dog(requests):
    return render(requests, 'create_dogs/create_dog_confirm_delete.html')

