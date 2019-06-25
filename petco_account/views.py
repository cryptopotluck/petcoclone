from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .forms import ProfilePictureUpdateForm, ProfileFrom, SocialMediaForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from tinymce.widgets import TinyMCE
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views import View
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from create_dogs.models import CreatePet
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'petco_account/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        email = request.POST['email']
        username = request.POST['userName']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Ceck if passwords match

        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'We have a copycat, username has been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use try recovering password.')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(email=email, username=username, password=password)
                    auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    user.save()
                    messages.success(request, 'You are now logged in please enhance your profile.')
                    return redirect('welcome')

        else:
            messages.error(request, 'We have a Bad Typer... Passwords do not match')
            return render(request, 'petco_account/register.html')
    else:
        return render(request, 'petco_account/register.html')


def profile(request):

    if request.method == 'POST':
        # uploaded_pic = request.FILES['profile_image2']
        profile_form = ProfileFrom(request.POST, instance=request.user.profile)
        # profile_picture_form = ProfilePictureUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        social_media_form = SocialMediaForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save(Profile.about)
            social_media_form.save(Profile.instagram)
            social_media_form.save(Profile.twitter)
            social_media_form.save(Profile.instagram)
            # profile_picture_form.save(Profile.profile_image)
            fs = FileSystemStorage()
            # fs.save(uploaded_pic)
    else:
        post = get_object_or_404(Profile, user_id=request.user)
        form = ProfileFrom(initial={'about': post.about, 'facebook': post.facebook, 'twitter': post.twitter,
                                    'instagram': post.instagram, 'profile_image2': post.profile_image})

        form.fields['about'].widget = TinyMCE()
        about = Profile.objects.get(user=request.user).about
        username = User.objects.get(username=request.user).username
        facebook_url = Profile.objects.get(user=request.user).facebook
        twitter_url = Profile.objects.get(user=request.user).twitter
        instagram_url = Profile.objects.get(user=request.user).instagram
        profile_pic = Profile.objects.get(user=request.user).profile_image
        pets = CreatePet.objects.filter(owner=request.user)
        paginator = Paginator(pets, 3)
        page = request.GET.get('page')
        my_pets = paginator.get_page(page)
        context = {
                'post': post,
                'form': form,
                'about': about,
                'username': username,
                'facebook_url': facebook_url,
                'twitter_url': twitter_url,
                'instagram_url': instagram_url,
                'profile_pic': profile_pic,
                'pets': my_pets,

        }

    return render(request, 'petco_account/profile.html', context)


class PetcoCreateView(CreateView):
    model = Profile
    fields = ['about', 'instagram', 'twitter', 'facebook', 'profile_image2']

    def get_form(self, form_class=ProfileFrom):
        form = super(PetcoCreateView, self).get_form(ProfileFrom)
        form.fields['about'].widget = TinyMCE()
        return form

    def form_invalid(self,form):
        errors = form.errors
        for error in errors:
            print(error)


class PetcoUpdateView(View):
    template_name = 'petco_account/profile_form_edit.html'


    def get(self, request):
        post = get_object_or_404(Profile, user_id=request.user)
        form = ProfileFrom(initial={'about': post.about, 'facebook': post.facebook, 'twitter': post.twitter, 'instagram': post.instagram, 'profile_image2': post.profile_image})

        form.fields['about'].widget = TinyMCE()
        about = Profile.objects.get(user=request.user).about
        username = User.objects.get(username=request.user).username
        facebook_url = Profile.objects.get(user=request.user).facebook
        twitter_url = Profile.objects.get(user=request.user).twitter
        instagram_url = Profile.objects.get(user=request.user).instagram
        profile_pic = Profile.objects.get(user=request.user).profile_image
        pets =  CreatePet.objects.filter(owner=request.user)
        paginator = Paginator(pets, 3)
        page = request.GET.get('page')
        my_pets = paginator.get_page(page)
        context = {
            'post': post,
            'form': form,
            'about': about,
            'username': username,
            'facebook_url':facebook_url,
            'twitter_url': twitter_url,
            'instagram_url': instagram_url,
            'profile_pic':profile_pic,
            'pets': my_pets,

        }
        return render(request, self.template_name, context)

    def post(self, request):

        if request.method == 'POST':
            # uploaded_pic = request.FILES['profile_image2']
            profile_form = ProfileFrom(request.POST, instance=request.user.profile)
            # profile_picture_form = ProfilePictureUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            social_media_form = SocialMediaForm(request.POST, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save(Profile.about)
                social_media_form.save(Profile.instagram)
                social_media_form.save(Profile.twitter)
                social_media_form.save(Profile.instagram)
                # profile_picture_form.save(Profile.profile_image)
                fs = FileSystemStorage()
                # fs.save(uploaded_pic)

        return redirect('update')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out, see you next time!')
        return redirect('login')


