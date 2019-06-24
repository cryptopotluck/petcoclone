from .models import PetPost
from django.contrib.auth.forms import UserCreationForm
from django import forms
from tinymce.widgets import TinyMCE


class PetPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PetPostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PetPost
        fields = ['pet', 'post_title', 'monetization', 'post_type', 'post_body', 'funding_goal']
        widgets = {
            'post_body': TinyMCE(),
        }
