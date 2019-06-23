from .models import CreatePet
from django.contrib.auth.forms import UserCreationForm
from django import forms
from tinymce.widgets import TinyMCE


class CreatePetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreatePetForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CreatePet
        fields = ['pet_name', 'pet_bread', 'pet_type', 'birthday', 'pet_profile_pic', 'about_pet']
        widgets = {
            'about_pet': TinyMCE(),
        }
