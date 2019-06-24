from django.shortcuts import render, redirect, reverse
from .models import PetPost
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from tinymce.widgets import TinyMCE
from .forms import PetPostForm

# Create your views here.

class PostCreateView(CreateView):
    model = PetPost
    fields = ['pet', 'post_title', 'monetization', 'post_type', 'post_body', 'funding_goal']

    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form(PetPostForm)
        form.fields['post_body'].widget = TinyMCE()
        return form

    def form_valid(self, form):
        # form.instance.author = self.request.user
        instance = form.save(commit=False)
        instance.pet_id = self.request.pet.id
        instance.save()
        response = super().form_valid(form)
        self.object.save()
        return response

    def form_invalid(self,form):
        errors = form.errors
        for error in errors:
            print(error)


def dog_post_detail(requests):
    return render(requests, 'dog_post/dog_post_detail.html')

def dog_post_edit_page(requests):
    return render(requests, 'dog_post/dog_post_form_edit.html')

def deleate_dog_post(requests):
    return render(requests, 'dog_post/dog_post_confirm_delete.html')