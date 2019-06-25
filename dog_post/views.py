from django.shortcuts import render, redirect, reverse
from .models import PetPost
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from tinymce.widgets import TinyMCE
from dog_post.forms import PetPostForm
from create_dogs.models import CreatePet
from django.contrib.auth.models import User

from petco_account.models import Profile

# Create your views here.


class PostCreateView(CreateView):
    model = PetPost
    fields = ['pet', 'post_title', 'monetization', 'post_type', 'post_body', 'funding_goal']

    def get_form(self, form_class=PetPostForm):
        form = super(PostCreateView, self).get_form(PetPostForm)
        form.fields['post_body'].widget = TinyMCE()

        # You need to handle what would happen if a non-authenticated user enters this page
        form.fields['pet'].queryset = CreatePet.objects.filter(
            owner=self.request.user
        )

        return form
    #
    # def form_valid(self, form, *kwargs):
    #     # form.instance.author = self.request.user
    #     instance = form.save(commit=False)
    #     instance.save()
    #     response = super().form_valid(form)
    #     self.object.save()
    #     return response

    # def post(self, request, *args, **kwargs):
    #     post = get_object_or_404(PetPost, pk=self.p)
    #     form = PetPostForm(request.POST)
    #
    #     if form.is_valid():
    #         post.pet = form.cleaned_data['pet']
    #         post.post_title = form.cleaned_data['post_title']
    #         post.post_type = form.cleaned_data['post_type']
    #         post.monetization = form.cleaned_data['monetization']
    #         post.funding_goal = form.cleaned_data['funding_goal']
    #         post.post_body = form.cleaned_data['post_body']
    #         post.save()
    #     return redirect('update')

    # def get_success_url(self):
    #     return reverse('update')
    #
    # def form_invalid(self,form):
    #     errors = form.errors
    #     for error in errors:
    #         print(error)


class DogPostDetailView(DetailView):
    model = PetPost


def dog_post_edit_page(request):
    return render(request, 'dog_post/dog_post_form_edit.html',)

def deleate_dog_post(requests):
    return render(requests, 'dog_post/dog_post_confirm_delete.html')

def pet_social(request):

    posts = PetPost.objects.all().values()
    post_picture = CreatePet.objects.all().values()
    post_owner = Profile.objects.all().values()
    # context['posts'] = PetPost.objects.filter().values().filter()
    user_username = User.objects.all().values()

    # paginator = Paginator(pets, 3)
    # page = request.GET.get('page')
    # my_pets = paginator.get_page(page)
    context = {
        'post_picture': post_picture,
        'post_owner': post_owner,
        'user_username': user_username,
        'posts': posts
        # 'pets': my_pets,

    }
    return render(request, 'dog_post/pet_social.html', context)