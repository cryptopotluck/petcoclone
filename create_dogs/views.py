from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import DetailView, CreateView, DeleteView
from tinymce.widgets import TinyMCE

from .forms import CreatePetForm
from .models import CreatePet
from dog_post.models import PetPost
from petco_account.models import Profile



# Create your views here.


class CreatePetPage(CreateView):
    model = CreatePet
    fields = ['pet_name', 'pet_bread', 'pet_type', 'birthday', 'pet_profile_pic', 'about_pet']

    def get_form(self, form_class=CreatePetForm):
        form = super(CreatePetPage, self).get_form(CreatePetForm)
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

    def form_invalid(self, form):
        errors = form.errors
        for error in errors:
            print(error)


class DogPage(DetailView):
    model = CreatePet

    def get_context_data(self, **kwargs):
        context = super(DogPage, self).get_context_data(**kwargs)
        # context['posts'] = PetPost.objects.filter().values().filter()
        posts = PetPost.objects.filter().values().filter()
        user_profile = Profile.objects.filter(user=self.request.user).values()

        context.update({
            'posts': posts,
            'user_profile': user_profile
        })
        return context


class PetEditPage(View):
    template_name = 'create_dogs/createpet_form_edit.html'

    def get(self, request, pk):
        pet = get_object_or_404(CreatePet, pk=pk, owner=request.user)
        print("get::pet_profile_pic", pet.pet_profile_pic)
        form = CreatePetForm(initial={'pet_name': pet.pet_name, 'pet_bread': pet.pet_bread, 'pet_type': pet.pet_type,
                                      'birthday': pet.birthday, 'pet_profile_pic': pet.pet_profile_pic,
                                      'about_pet': pet.about_pet})

        form.fields['about_pet'].widget = TinyMCE()

        context = {
            'pet': pet,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        pet = get_object_or_404(CreatePet, pk=pk)
        form = CreatePetForm(request.POST, request.FILES)

        if form.is_valid():
            pet.pet_name = form.cleaned_data['pet_name']
            pet.pet_bread = form.cleaned_data['pet_bread']
            pet.pet_type = form.cleaned_data['pet_type']
            if str(form.cleaned_data.get('pet_profile_pic')) != \
                    str(CreatePet.pet_profile_pic.field.default):
                pet.pet_profile_pic = form.cleaned_data['pet_profile_pic']
            pet.about_pet = form.cleaned_data['about_pet']
            pet.birthday = form.cleaned_data['birthday']

            pet.save()
        return redirect('update')


def dog_heaven(requests):
    return render(requests, 'create_dogs/dog_heaven.html')


class PetDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CreatePet
    success_url = '/account/update'

    def test_func(self):
        pet = self.get_object()
        if self.request.user == pet.owner:
            return True
        return False
