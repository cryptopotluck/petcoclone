
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from tinymce.widgets import TinyMCE


class ProfileFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileFrom, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['about', 'facebook', 'twitter', 'instagram', 'profile_image']
        widgets = {
            'about': TinyMCE(),
        }


class ProfilePictureUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # profile_image = forms.FileInput()
        fields = ['profile_image']


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('facebook', 'twitter', 'instagram')


class ImageUploadForm(forms.Form):
    image = forms.ImageField()